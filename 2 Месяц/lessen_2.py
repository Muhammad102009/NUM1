" База Данных "
" СУБД - Система управления базой данный "
" CRUD - CREATE, RETRIVE, UPTADE, DELETE "

import sqlite3

connect = sqlite3.connect("itpark.db")
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS itpark(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALCE,
        rating DOUBLE (4,2) DEFAULT (0.0),
        brith_date DATE
    )
""")

def register():
    ful_name = input("Введите ФИО: ")
    age = int(input("Введите свой возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    rating = float(input("Введите свой рейтинг: "))
    brith_date = input("Введите дату рождение: ")

    cursor.execute(f""" INSERT INTO itpark
                   (full_name, age, direction, is_have, rating, brith_date)
                   VALUES ('{ful_name}','{age}','{direction}','{is_have}','{rating}','{brith_date}')
""")
    connect.commit()
register()