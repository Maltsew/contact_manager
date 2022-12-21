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
    
def display_DB_info():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    SELECT * FROM users
    ''')
    df = pd.DataFrame(c.fetchall())
    print(df)
    
def create_test_user():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    INSERT INTO users (user_id, user_name, user_email, user_phone)
    
    VALUES
    (1, 'Maltsev Nikita Andreevich', 'maltsev@lan.po', '1-14-08'),
    (2, 'Test TEst TEST', 'Test@lan.po', '1-12-08')
    ''')
    conn.commit()
    
def drop_user_table():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute(
    '''
    DROP TABLE users
    ''')
    conn.commit()
    