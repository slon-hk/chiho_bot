import sqlite3
from datetime import datetime, date

def start():
    conn = sqlite3.connect(r"chiho_bot\db_chiho.sql")
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                tg_id TEXT, 
                data TEXT, houre REAL)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS rate (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                tg_id TEXT UNIQUE, 
                rate INTEGER)""")
    conn.commit()
    cur.close()
    conn.close()

def fill_rate(tg_id, rate: int):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO rate (tg_id, rate) VALUES ('%s', '%s')" % (tg_id, rate))
    conn.commit()
    cur.close()

def fill_houre(tg_id, houre: float ):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO users (data, houre, tg_id) VALUES ('%s', '%s', '%s')""" % (datetime.now().strftime("%Y.%m.%d"), houre, tg_id))
    conn.commit()
    cur.close()

def get_rate(tg_id):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM rate WHERE tg_id = {tg_id};")
    rate = cur.fetchall()[0][2]
    conn.close()
    return rate

def user_exists(tg_id):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    cur.execute("SELECT * FROM rate WHERE tg_id = ?", (tg_id,))
    user = cur.fetchone()
    conn.close()
    
    return user is not None

def get_hours(tg_id):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    
    # Используем параметризованный запрос для безопасности
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    info = cur.fetchall()
    conn.close()

    all_hours = 0
    result = "Дата             | Часы\n"
    
    today = date.today()
    current_month = today.month
    current_year = today.year

    for row in info:
        data_date = datetime.strptime(row[2], "%Y.%m.%d").date()  # Предполагаем, что даты хранятся в формате ГГГГ.ММ.ДД
        hours = int(row[3])
        
        # Проверяем, принадлежит ли дата текущему месяцу и году
        if data_date.month == current_month and data_date.year == current_year:
            result += f"{data_date} | {hours}\n"
            all_hours += hours

    rate = int(get_rate(tg_id=tg_id))
    total_salary = all_hours * rate
    return result + f"\nЗарплата: { '{:,.0f}'.format(total_salary) }"


def delete_user(tg_id):
    # Подключение к базе данных
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()

    try:
        # Выполнение команды удаления
        cur.execute("DELETE FROM rate WHERE tg_id = ?", (tg_id,))
        
        # Сохранение изменений
        conn.commit()
        
        # Проверка успешности удаления
        if cur.rowcount > 0:
            print(f"Пользователь с tg_id={tg_id} успешно удален.")
        else:
            print(f"Пользователь с tg_id={tg_id} не найден.")
    
    except sqlite3.Error as error:
        print(f"Ошибка при удалении пользователя: {error}")
    
    finally:
        # Закрытие соединения
        conn.close()