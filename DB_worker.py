# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:22:19 2022

@author: n.maltsev
"""


import sqlite3
import pandas as pd
from bcolors import bcolors
#from DB_logic import selected_db



#global selected_db
#database_name = selected_db
selected_db = 'contacts.db'

def create_table_user():
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Создает таблицу users, если таблица еще не создана.
    таблица users содержит поля:
        user_id тип INTEGER PRIMARY KEY,
        user_name тип данных TEXT,
        user_email тип данных TEXT,
        user_phone тип данных TEXT'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    CREATE TABLE IF NOT EXISTS users
    ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [user_email] TEXT, [user_phone] TEXT)
    ''')
    conn.commit()
    
def select_all_contacts():
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет запрос на получение всех данных из таблицы users.
    Полученные данные преобразуются в объект DataFrame библиотеки Pandas.
    Возвращает True, если DataFrame не пуст., все данные выводятся в терминал
    функцией print().
    Иначе возвращает False
    '''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    SELECT user_name, user_email, user_phone FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    if len(df) != 0:
        df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
        print(f"{bcolors.OKCYAN}",f"{bcolors.UNDERLINE}", df, f"{bcolors.ENDC}")
        return True
    else:
        return False

    
    
def add_contact_to_table(contact_name, contact_email, contact_phone):
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет вставку аргументов (contact_name, contact_email, contact_phone)
    в таблицу users в соответствующте поля
    (user_name, user_email, user_phone)'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute("INSERT INTO users (user_name, user_email, user_phone)\
              VALUES (?, ?, ?)",
              (contact_name, contact_email, contact_phone))
    conn.commit()
    
def drop_user_table():
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет удаление таблицы users'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    DROP TABLE users
    ''')
    conn.commit()
    
def contact_search_query(contact_info):
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет запрос на поиск информации о контакте в соответствии с заданной
    подстрокой contact_info. Поиск происходит по всем полям БД users, т.е.
    подстрока проверяется по каждому из имеющихся в таблице полей.
    Результат запроса преобразуется в в объект DataFrame библиотеки Pandas.
    Если DataFrame не пуст, принтует результат поиска в терминал и возаращет
    True, иначе принтует сообщение и возвращает False'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    # паттерн - информация польз., которая может находится в любом месте в поле таблицы users
    pattern = '%' + str(contact_info) + '%'
    c.execute("SELECT user_name, user_email, user_phone FROM users \
              WHERE user_name LIKE ? OR user_email LIKE ? OR user_phone LIKE ?",
              (pattern, pattern, pattern)
              )
    df = pd.DataFrame(c.fetchall())
    if len(df) != 0:
        df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
        print(f"{bcolors.OKCYAN}",f"{bcolors.UNDERLINE}", df, f"{bcolors.ENDC}")
        return True
    else:
        print(f"{bcolors.FAIL}",'           Поиск', contact_info, ' не вернул результата!', f"{bcolors.ENDC}")
        return False
        
def delete_contact_query(contact_name, conctact_email):  
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет запрос на удаление информации о контакте в соответствии с заданными
    подстроками contact_name, conctact_email. Подстроки должны точно соответствовать
    имеющимся в базе значениям'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE user_name = ? AND user_email = ?",
              (contact_name, conctact_email)
              )
    conn.commit()
    
def contact_verification_query(contact_name, conctact_email):
    
    '''  Подключается к БД с именем selected_db с помощью sqlite3 драйвера. 
    Выполняет запрос для получения из БД контакта с данными, в точности
    соответствующим введенным пользователем ФИО и эл. почты
    Назначение функции - проверка, имеется ли конкретный контакт в таблице users'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute("SELECT user_name, user_email FROM users \
              WHERE user_name = ? AND user_email = ?",
              (contact_name, conctact_email)
              )
    if len(c.fetchall()) != 0:
        return True
    return False
    
    
def select_all_contacts_for_export(file_name='default'):
    
    ''' Подключается к БД с именем selected_db с помощью sqlite3 драйвера.
    Выполняет запрос на получение всех данных из таблицы users.
    Полученные данные преобразуются в объект DataFrame библиотеки Pandas.
    Далее для DataFrame вызывается метод, преобразующий его в excel с именем,
    заданным пользователем через терминал. Если users не содержит ни одной
    записи, в excel будет записано ничего, т.е. просто создан файл с введенным
    именем
    excel файлу необходимо задать валидное имя,'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    SELECT user_name, user_email, user_phone FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    try:
        excel_file_name = str(file_name) + ".xlsx"
        df.to_excel(excel_file_name, sheet_name="Contacts")
        return True
    except ValueError:
        print(f"{bcolors.FAIL}Имя не может быть пустым!{bcolors.ENDC}")
        return False        
            