import sqlite3
from datetime import datetime, date
import logging

# Set up logging
logger = logging.getLogger(__name__)

def start():
    # Connect to the SQLite database
    conn = sqlite3.connect(r"chiho_bot\db_chiho.sql")
    cur = conn.cursor()

    # Create users table if it doesn't exist
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id TEXT,
                data TEXT, houre REAL)""")
    logger.info("Table 'users' checked/created.")

    # Create rate table if it doesn't exist
    cur.execute("""CREATE TABLE IF NOT EXISTS rate (id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id TEXT UNIQUE,
                rate INTEGER)""")
    logger.info("Table 'rate' checked/created.")

    conn.commit()
    cur.close()
    conn.close()
    logger.info("Database connection closed.")

def fill_rate(tg_id, rate: int):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Insert the rate into the rate table
    cur.execute("INSERT INTO rate (tg_id, rate) VALUES (?, ?)", (tg_id, rate))
    logger.info("Rate inserted for tg_id=%s: %d", tg_id, rate)

    conn.commit()
    cur.close()
    conn.close()
    logger.info("Database connection closed after filling rate.")

def fill_houre(tg_id, houre: float):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Insert the hours into the users table
    cur.execute("INSERT INTO users (data, houre, tg_id) VALUES (?, ?, ?)",
                (datetime.now().strftime("%Y.%m.%d"), houre, tg_id))
    logger.info("Hours inserted for tg_id=%s: %f", tg_id, houre)

    conn.commit()
    cur.close()
    conn.close()
    logger.info("Database connection closed after filling hours.")

def get_rate(tg_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Retrieve the rate for the given tg_id
    cur.execute("SELECT * FROM rate WHERE tg_id = ?", (tg_id,))
    rate = cur.fetchone()
    conn.close()
    logger.info("Rate retrieved for tg_id=%s: %d", tg_id, rate[2] if rate else -1)

    return rate[2] if rate else None

def user_exists(tg_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Check if the user exists in the rate table
    cur.execute("SELECT * FROM rate WHERE tg_id = ?", (tg_id,))
    user = cur.fetchone()
    conn.close()
    logger.info("User existence check for tg_id=%s: %s", tg_id, "exists" if user else "does not exist")

    return user is not None

def get_hours(tg_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Retrieve hours worked by the user from the users table
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    info = cur.fetchall()
    conn.close()
    logger.info("Hours retrieved for tg_id=%s", tg_id)

    all_hours = 0
    result = "Дата             | Часы\n"

    today = date.today()
    current_month = today.month
    current_year = today.year

    for row in info:
        data_date = datetime.strptime(row[2], "%Y.%m.%d").date()
        hours = float(row[3])

        if data_date.month == current_month and data_date.year == current_year:
            result += f"{data_date} | {hours}\n"
            all_hours += hours

    rate = int(get_rate(tg_id=tg_id))
    total_salary = all_hours * rate
    logger.info("Total hours and salary calculated for tg_id=%s", tg_id)
    return result + f"\nЗарплата: { '{:,.0f}'.format(total_salary) }"

def delete_user(tg_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    try:
        # Delete the user from the rate table
        cur.execute("DELETE FROM rate WHERE tg_id = ?", (tg_id,))
        conn.commit()
        if cur.rowcount > 0:
            logger.info("User with tg_id=%s successfully deleted.", tg_id)
            print(f"Пользователь с tg_id={tg_id} успешно удален.")
        else:
            logger.warning("User with tg_id=%s not found.", tg_id)
            print(f"Пользователь с tg_id={tg_id} не найден.")
    except sqlite3.Error as error:
        logger.error("Error deleting user with tg_id=%s: %s", tg_id, error)
        print(f"Ошибка при удалении пользователя: {error}")
    finally:
        conn.close()
        logger.info("Database connection closed after deleting user.")

def all_stats(tg_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    # Retrieve all hours worked by the user from the users table
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    info = cur.fetchall()
    conn.close()
    logger.info("All hours retrieved for tg_id=%s", tg_id)

    all_hours = 0
    result = "Дата             | Часы\n"

    for row in info:
        data_date = datetime.strptime(row[2], "%Y.%m.%d").date()
        hours = float(row[3])
        result += f"{data_date} | {hours}\n"
        all_hours += hours

    rate = int(get_rate(tg_id=tg_id))
    total_salary = all_hours * rate
    logger.info("Total hours and salary calculated for all time for tg_id=%s", tg_id)
    return result + f"\nЗарплата: { '{:,.0f}'.format(total_salary) }"