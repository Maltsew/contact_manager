# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:38:43 2022

@author: n.maltsev

Модуль вызова основных команд приложения.
Из-за особенности взаимодействия с парсером командной строки из модуля
cl_parser (После создания объекта парсера командной строки, основные аргументы
добавляются посредством вызова add_argument к объекту парсера, таким образом
объект парсера обладает доступом ко всем аргументам). Для того, чтобы осуществить
вызов конкретного аргумента парсера командной строки, необходимо ожидать ввода
в терминал этого аргумента без дополнительных аргументов (не предусмотренных
парсером); В случае вызова нескольких аргументов парсера одновременно, они
будут вызваны поочередно.
Использование парсера командной строки выглядит так:
    Вызов аргумента парсера (например: -a) надо вызывать без дополнительных
    аргументов (как если: -а Иванов Иван Иванович). В таком случае парсер
    каждой функции переходит в else и в терминал будет выведена ошибка
    Если не осуществить вызов ни одного аргумента, парсер возвращает
    false и не выполняет никаких действий
"""


from DB_worker import *
from cl_parser import parse_command_line
from contacts_manager import *
from DB_logic import db_selector, create_new_database
from bcolors import bcolors

# Объект парсера командной строки
space = parse_command_line()


def command_add_contact():
    
    ''' Вызов добавления нового контакта происходит при вводе в терминал
    аргумента -а парсера командной строки.
    Вызов должен быть без дополнительных аргументов (см. документацию модуля
    main_commands)
    '''
    
    create_table_user()
    if space.add_contact == '':
        add_contact()
    elif space.add_contact == None:
        return False
    else:
        print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}",
              'Недопустимый ввод для добавления нового контакта --->',
                f"{space.add_contact}", f"{bcolors.ENDC}")
        
def command_show_contact():
    
    ''' Вызов предоствления списка всех контактов происходит при вводе в терминал
    аргумента -ls парсера командной строки.
    Вызов должен быть без дополнительных аргументов (см. документацию модуля
    main_commands)
    '''
    
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
        print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}",
              'Недопустимый ввод для отображения списка контактов --->',
                f"{space.show_contacts}", f"{bcolors.ENDC}")
        

def command_find_contact():
    
    ''' Вызов поиска контакта происходит при вводе в терминал
    аргумента -find парсера командной строки.
    Вызов должен быть без дополнительных аргументов (см. документацию модуля
    main_commands)
    '''
    
    create_table_user()
    if space.find_contact == '':
        search_inquiry()
    elif space.find_contact == None:
        return False
    else:
        print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}",
              'Недопустимый ввод для поиска контакта --->',
                f"{space.find_contact}", f"{bcolors.ENDC}")
        

def command_remove_contact():
    
    ''' Вызов удаления контакта происходит при вводе в терминал
    аргумента -rm парсера командной строки.
    Вызов должен быть без дополнительных аргументов (см. документацию модуля
    main_commands)
    '''
    
    create_table_user()
    if space.remove_contact == '':
        delete_contact()
    elif space.remove_contact == None:
        return False
    else:
        print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}",
              'Недопустимый ввод для удаления контакта --->',
                f"{space.remove_contact}", f"{bcolors.ENDC}")
        
        
def command_export_contacts():
    
    ''' Вызов экспорта контактов происходит при вводе в терминал
    аргумента -export парсера командной строки.
    Вызов должен быть без дополнительных аргументов (см. документацию модуля
    main_commands)
    '''
    
    create_table_user()
    if space.export_contact == '':
        export_contacts()
    elif space.export_contact == None:
        return False
    else:
        print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}",
              'Недопустимый ввод для экспорта контактов --->',
                f"{space.export_contact}", f"{bcolors.ENDC}")
        
        
# def command_change_database():
#     #create_table_user()
#     if space.change_database == '':
#         # Убрал. Нужно доработать механизм выбора бд
#         pass
#         # вызван селектор баз, вернет имя выбранной базы или создаст новую если таковой нет и вернет ее имя
#          # db_selector()
#     elif space.change_database == None:
#         return False
#     else:
#         print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
#         # print(f"{bcolors.FAIL}",
#         #       'Недопустимый ввод для экспорта контактов --->',
#         #         f"{space.export_contact}", f"{bcolors.ENDC}")
        
# def command_create_database():
#     #create_table_user()
#     if space.create_database == '':
#         # Убрал. Нужно доработать механизм выбора бд
#         pass
#         #create_new_database()
#     elif space.create_database == None:
#         return False
#     else:
#         print(f"{bcolors.FAIL}Ошибка!{bcolors.ENDC}")
#         # print(f"{bcolors.FAIL}",
#         #       'Недопустимый ввод для экспорта контактов --->',
#         #         f"{space.export_contact}", f"{bcolors.ENDC}")
    
