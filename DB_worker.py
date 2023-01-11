# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:22:19 2022

@author: n.maltsev
"""


import sqlite3
import pandas as pd
#from DB_logic import selected_db



#global selected_db
#database_name = selected_db
selected_db = 'contacts.db'

def create_table_user():
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    CREATE TABLE IF NOT EXISTS users
    ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [user_email] TEXT, [user_phone] TEXT)
    ''')
    conn.commit()
    
def select_all_contacts():
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    SELECT user_name, user_email, user_phone FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    if len(df) != 0:
        df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
        print(df)
        return True
    else:
        return False

    
    
def add_contact_to_table(contact_name, contact_email, contact_phone):
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute("INSERT INTO users (user_name, user_email, user_phone)\
              VALUES (?, ?, ?)",
              (contact_name, contact_email, contact_phone))
    conn.commit()
    
def drop_user_table():
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    DROP TABLE users
    ''')
    conn.commit()
    
def contact_search_query(contact_info):
    ''' Выполняет запрос на поиск информации о контакте в соответствии с заданным
    паттерном contact_info. Поиск происходит по всем полям БД users (с целью
    ускороить поиск)'''
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    pattern = '%' + str(contact_info) + '%'
    c.execute("SELECT user_name, user_email, user_phone FROM users \
              WHERE user_name LIKE ? OR user_email LIKE ? OR user_phone LIKE ?",
              (pattern, pattern, pattern)
              )
    df = pd.DataFrame(c.fetchall())
    if len(df) != 0:
        df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
        print(df)
        return True
    else:
        print('           Поиск', contact_info, 'не вернул результата!')
        return False
        
def delete_contact_query(contact_name, conctact_email):  
    
    ''' Выполняет запрос на удаление контактов в БД в соответствии с заданным
    паттерном contact_info'''
    
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE user_name = ? AND user_email = ?",
              (contact_name, conctact_email)
              )
    conn.commit()
    
def contact_verification_query(contact_name, conctact_email):
    
    ''' Запрос для проверки наличия в БД контакта с данными, в точности
    соответствующим введенным пользователем'''
    
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
    conn = sqlite3.connect(selected_db)
    c = conn.cursor()
    c.execute(
    '''
    SELECT user_name, user_email, user_phone FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    if len(df) != 0:
        try:
            excel_file_name = str(file_name) + ".xlsx"
            df.to_excel(excel_file_name, sheet_name="Contacts")
        except ValueError:
            print('Имя не может быть пустым')
            return False
            
            