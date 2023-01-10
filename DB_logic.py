# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:24:58 2022

@author: n.maltsev
"""

from pathlib import Path
import glob, os
#from typing import Union
import sys




def get_project_root()->Path:
    
    ''' Возвращает относительное расположение main.py'''
    
    return Path("__main.py__").parent.parent

def database_browser():
    
    ''' Функция перебора списка всех БД, находящихся в корневом каталоге (со
    скриптом)'''
    
    root = get_project_root()
    os.chdir(root)
    # список для хранения перечня всех бд
    database_count = []
    # перебор всех файлов с расширением .db
    for file in glob.glob("*.db"):
        database_count.append(file)
    if len(database_count) != 0:
        keys = list(range(len(database_count)))
        # кладем имена всех бд в значения словаря, ключи - числа в диапазоне keys 
        d = dict(zip(keys, database_count))
        # При наличии бд вернем словарь, иначе - None
        return d


def db_is_exist():
    ''' Если в каталоге существует хоть одна бд, возвращает True
    Иначе возвращает False'''
    database = database_browser()
    if database is not None:
        return True
    print('База данных еще не создана!')
    return False


def print_database_list():
    ''' Принтует список всех баз в каталоге проекта db_is_exist
    вернул True'''
    is_exist = db_is_exist()
    if is_exist:
        # Создает еще один объект перебора всех бд, чтобы получить словарь баз
        # плохая логика, но больше возможностей для обработки вывода информации
        database = database_browser()
        for key, value in database.items():
            print(key,' -> ', value)
            

def db_selector():
    ''' Возвращает название выбранной по индексу из словаря базы данных'''
    print_database_list()
    is_exist = db_is_exist()
    if is_exist:
        try:
            selected_num = int(input('Выберите номер базы данных для работы: '))
            chosen_base = database_browser()
            if selected_num in chosen_base:
                #print(chosen_base[selected_num])
                return chosen_base[selected_num]
            else:
                print('Невозможно выбрать базу', selected_num)
                print('Существующие базы: ')
                print_database_list()
        except ValueError:
            print('Ошибка ввода данных!')
            print('Существующие базы: ')
            print_database_list()
    else:
        return create_new_database()
            

def create_new_database():
    print('Будет создана новая база данных контактов')
    create_db_confirm = input('Продолжить? (Y / N): ')
    if create_db_confirm in ('Y', 'Yes', 'y', 'yes', 'YES'):
        new_db_name = input('Введите название: ')
        new_db_name = new_db_name + '.db'
        return new_db_name


selected_db = db_selector()