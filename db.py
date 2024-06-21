import sqlite3
from datetime import datetime, date

def start():
    conn = sqlite3.connect("db_chiho.sql")
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

def get_houre(tg_id):
    conn = sqlite3.connect("db_chiho.sql")
    cur = conn.cursor()
    
    # Используем параметризованный запрос для безопасности
    cur.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
    info = cur.fetchall()
    conn.close()

    all_houre = 0
    result = "Дата             | Часы\n"
    
    today = date.today()  # Получаем текущую дату без времени
    
    for row in info:
        data_date = datetime.strptime(row[2], "%Y.%m.%d").date()  # Предполагаем, что даты хранятся в формате ГГГГ-ММ-ДД
        houre = int(row[3])
        result += f"{data_date} | {houre}\n"
        
        if data_date == today:
            all_houre += houre

    rate = int(get_rate(tg_id=tg_id))
    all_houre *= rate
    return result + f"\nЗарплата: { '{:,.0f}'.format(all_houre)}"