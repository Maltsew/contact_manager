# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:22:19 2022

@author: n.maltsev
"""


import sqlite3
import pandas as pd


def create_table_user():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    CREATE TABLE IF NOT EXISTS users
    ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [user_email] TEXT, [user_phone] TEXT)
    ''')
    conn.commit()
    
def select_all_contacts():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    SELECT user_name, user_email, user_phone FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
    print(df)

    
    
def add_contact_to_table(contact_name, contact_email, contact_phone):
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute("INSERT INTO users (user_name, user_email, user_phone)\
              VALUES (?, ?, ?)",
              (contact_name, contact_email, contact_phone))
    conn.commit()
    
def drop_user_table():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    DROP TABLE users
    ''')
    conn.commit()
    
def contact_search(contact_info):
    conn = sqlite3.connect('database')
    c = conn.cursor()
    #c.execute("SELECT user_name, user_email, user_phone FROM users WHERE user_name = ? OR user_email = ? OR user_phone = ?",
    pattern = '%' + str(contact_info) + '%'
    c.execute("SELECT user_name, user_email, user_phone FROM users WHERE user_name LIKE ? OR user_email LIKE ? OR user_phone LIKE ?",

              (pattern, pattern, pattern)
              )
    df = pd.DataFrame(c.fetchall())
    df.columns = ['ФИО', 'Адрес эл. почты', 'Телефон']
    print(df)
    