# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:24:58 2022

@author: n.maltsev
"""

from pathlib import Path
import glob, os


DB_name = 'database.db'

def database_choice(database_name=DB_name):
    ''' Функция для выбора базы данных. На входе - имя по умолчанию.
    По выбору пользователя имя можно сменить, тогда функция вернет новое
    имя'''
    
    

def database_browser():
    ''' Функция просмотра списка всех БД, находящихся в корневом каталоге (со
    скриптом)'''
    # root = get_project_root()
    # os.chdir(root)
    # all_database = []
    # for file in glob.glob("*.db"):
    #     all_database.append(file)
    # for db in all_database:
    #     print(db)
    # if len(all_database) != 0:
    #     return all_database
    # else:
    #     print('Еще не создано ни одной базы для хранения контактов')
    root = get_project_root()
    os.chdir(root)
    all_database = dict()
    database_count = []
    for file in glob.glob("*.db"):
        database_count.append(file)
    all_databases = dict()
    for n in range(len(database_count)):
        for db in database_count:
            all_databases.update({'db%s'%n:db})
    
            
    
    
def get_project_root():
    return Path("__main.py__").parent.parent
