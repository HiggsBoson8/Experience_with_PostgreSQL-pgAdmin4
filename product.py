import requests
import psycopg2
from random import randint, choice
from datetime import datetime

fruits_list = ["Яблоко", "Апельсин", "Банан", "Мандарин", "Груша", "Клубника", "Персик", "Лимон", 
    "Ананас", "Виноград", "Вишня", "Облепиха", "Киви", "Лайм", "Морковь", "Кабачок", 
    "Тыква", "Редис", "Горох", "Грибы", "Сахар", "Соль", "Перец", "Зелень", 
    "Оливковое масло", "Консерва", "Соус", "Сладость", "Булочка", "Хлеб", "Кофе", "Чай", 
    "Йогурт", "Молоко", "Сыр", "Яичные продукты", "Газировка", "Искусственный сахар", "Замороженные овощи", 
    "Замороженные фрукты", "Сухарик", "Цуката", "Кекс", "Пастил", "Мармелад", "Шоколад", "Конфеты", "Вафли"]

generate_description = [
    "На заводе", "В наличии", "На складе", "В магазине", "На фабрике", "На точке"
]

# Вручную
# Создать базу данных mega owner username;
# create database mega owner abay;
# Сделайте GRANT
# GRANT ALL PRIVILEGES ON DATABASE mega to abay;

# Python
# Создать таблтицу product
# Записать 

# Connection to the PostgreSQL database
connection = psycopg2.connect(
    host = "localhost",
    user = "abay",
    password = "123",
    database = "mega"
)
cursor = connection.cursor()

# Создать таблицу, если она не существует
cursor.execute("CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, title VARCHAR(50), \
description TEXT, price INT, create_ad TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)")

for i in fruits_list:
    title = i
    # description = "{}, {}".format(choice(generate_description), choice(generate_description))
    description = f"{choice(generate_description)} {choice(generate_description)}"
    price = randint(1000, 3000)
    create_ad = datetime.now().strftime("%Y.%m.%d %H:%M:%S")

    # Вставьте инфориацию о продукте в таблицу
    cursor.execute("INSERT INTO product (title, description, price, create_ad) \
    VALUES (%s, %s, %s, %s)", (title, description, price, create_ad))

    # Зафиксируйте изменения в базе данных
    connection.commit()

# Закройте курсор и соединение 
cursor.close()
connection.close()






