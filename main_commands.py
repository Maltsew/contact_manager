# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:38:43 2022

@author: n.maltsev
"""


from DB_worker import *
from cl_parser import parse_command_line
from contacts_manager import *
from DB_logic import db_selector, create_new_database


space = parse_command_line()


def command_add_contact():
    create_table_user()
    if space.add_contact == '':
        add_contact()
    elif space.add_contact == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для добавления нового контакта --> {space.add_user}")
        
def command_show_contact():
    create_table_user()
    if space.show_contacts == '':
        all_contacts = select_all_contacts()
        if not all_contacts:
            print('В базе нет ни одного контакта!')
            return False
        return True
    elif space.show_contacts == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для показа списка всех контактов --> {space.show_contacts}")
        

def command_find_contact():
    create_table_user()
    if space.find_contact == '':
        search_inquiry()
    elif space.find_contact == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для поиска контактов --> {space.find_contact}")
        

def command_remove_contact():
    create_table_user()
    if space.remove_contact == '':
        delete_contact()
    elif space.remove_contact == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для поиска контактов --> {space.remove_contact}")
        
        
def command_export_contacts():
    create_table_user()
    if space.export_contact == '':
        export_contacts()
    elif space.export_contact == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для экспорта контактов --> {space.export_contact}")
        
        
def command_change_database():
    #create_table_user()
    if space.change_database == '':
        # вызван селектор баз, вернет имя выбранной базы или создаст новую если таковой нет и вернет ее имя
         p = db_selector()
         print(p)
    elif space.change_database == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для выбора базы данных --> {space.change_database}")
        
def command_create_database():
    #create_table_user()
    if space.create_database == '':
        # вызван селектор баз, вернет имя выбранной базы или создаст новую если таковой нет и вернет ее имя
        create_new_database()
    elif space.create_database == None:
        return False
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для выбора базы данных --> {space.create_database}")
    
