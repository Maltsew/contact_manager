# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:16:21 2022

@author: n.maltsev

Модуль для реализации взаимодейтсвия данных, полученных от пользователя
и данными из БД sqlite3.
Модуль содержит функции-контроллеры. Полученные от пользователя данные проходят
валидацию и проверку на правильность ввода. Валидированные данные передаются 
как аргументы в функции модуля взаимодействия с БД DB_worker.

"""


from cl_parser import parse_command_line
from DB_worker import *
from contact_validators import *
from bcolors import bcolors
from typing import NewType
import pandas as pd

# Пользовательский тип возвращаемых данных - DataFrame
DataFrame = NewType('DataFrame', pd.core.series.Series)



def validate_contact() -> bool:
    
    ''' Функция реализует проверку введенных пользователем данных.
    1) Вызов contact_name_is_cyrrilic для введенного ФИО
    2) Вызов contact_email_is_valid для адреса эл. почты
    3) Вызов contact_phone_is_valid для телефона
    Валидация происходит поочередно 1), 2) и 3), и если все
    пункты пройдены - возвращает True,
    Иначе возвращает сообщение о несоответствии введенным данным и
    False для проверки каждого пунка валидатора
    '''
    
    try:
        new_contact_name, new_contact_email, new_contact_phone = contact_info_insertion()
        if contact_name_is_cyrrilic(new_contact_name):
            if contact_email_is_valid(new_contact_email):
                if contact_phone_is_valid(new_contact_phone):
                    return True
                else:
                    print(f"{bcolors.FAIL}Номер телефона введен неверно!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Адрес почты введен неверно!{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}ФИО введено неверно!{bcolors.ENDC}")
    except TypeError:
        print(f"{bcolors.FAIL}Ошибка ввода данных!{bcolors.ENDC}")
    return False

    
def add_contact() -> None:
    
    ''' После проверки на валидность, добавляет контакт в БД
    посредством вызова add_contact_to_table из модуля взаимодействия
    с БД DB_worker
    После добавления в таблицу users выводит сообщение об успешном
    добавлении контакта'''
    
    if validate_contact():
        contact_name, contact_email, contact_phone = data
        add_contact_to_table(contact_name=contact_name,
                             contact_email=contact_email,
                             contact_phone=contact_phone)
        print(f"{bcolors.OKGREEN}Контакт добавлен!{bcolors.ENDC}")
    
    
def show_all_contacts() -> DataFrame:
    
    ''' посредством вызова select_all_contacts из модуля взаимодействия
    с БД DB_worker получает список всех имеющихся в таблице users контактов
    в виде обхекта DataFrame'''
    
    all_contacts_info = select_all_contacts()
    return all_contacts_info


def contact_info_insertion() -> tuple:
    
    ''' Добавление нового контакта
    Последовательно принимает от пользователя данные о контакте
    Полученные данные кладутся в кортеж data, который хранит их для
    дальнейшего использования функцией add_contact.'''
    
    input_name = input('Введите ФИО: ')
    input_email = input('Введите адрес электронной почты: ')
    input_phone = input('Введите номер телефона:')
    global data
    data = (input_name, input_email, input_phone)
    return data

def search_inquiry() -> None:
    
    ''' Поисковой запрос - информация от пользователя о контакте (Данные о ФИО,
    почте либо телефоне)
    Введенная информация, если она есть и не пустая, посредством вызова
    contact_search_query из модуля взаимодействия с БД DB_worker передается
    в запрос поиска по таблице users.
    Поиск осуществляется по всем полям по ключевому слову (см. документацию
    contact_search_query). Если запрос пустой - возвращает сообщение об ошибке'''
    
    search_info = input('Введите информацию о контакте: ')
    print(f"{bcolors.OKCYAN}                  Результат поиска:{bcolors.ENDC}")
    if search_info != '':
        contact_search_query(contact_info=search_info)
    else:
        #print('Пустой поисковой запрос!')
        print(f"{bcolors.FAIL}Пустой поисковой запрос!{bcolors.ENDC}")
    
def delete_contact() -> None:
    
    ''' Функция удаления контакта из таблицы users
    Удаление происходит в 2 этапа:
        1) Пользователь вводит информацию о контакте, который следует удалить.
    Посредством вызова contact_verification_query из модуля взаимодействия
    с БД DB_worker список всех контактов, удовлетворяющих поисковому запросу,
    выводится пользователю в терминал.
        2) На втором этапе происходит непосредственно удаление:
    Посредством вызова delete_contact_query из модуля взаимодействия
    с БД DB_worker происходит запрос на удалениие данных (см. документацию
    delete_contact_query модуля DB_worker), в точности соответсвующих
    введенным пользователем в запросе на удаление'''
    
    delete_info = input('Введите информацию о контакте: ')
    print(f"{bcolors.OKCYAN}                  Результат поиска:{bcolors.ENDC}")
    if delete_info != '':
        contact_search_query(contact_info=delete_info)
        contact_name_to_del = input('Введите полное имя контакта: ')
        contact_email_to_del = input('Введите точный адрес эл. почты: ')
        print(f"{bcolors.WARNING}", 'Будет удален контакт ',
              contact_name_to_del, contact_email_to_del , f"{bcolors.ENDC}")

        deletion_confirm = input('Продолжить? (Y / N): ')
        if deletion_confirm in ('Y', 'Yes', 'y', 'yes', 'YES'):
            if contact_verification_query(contact_name=contact_name_to_del, conctact_email=contact_email_to_del):
                delete_contact_query(contact_name=contact_name_to_del, conctact_email=contact_email_to_del)
                print(f"{bcolors.OKGREEN}Контакт удален!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Ошибка ввода данных!{bcolors.ENDC}")
                print(f"{bcolors.FAIL}", 'Информация о контакте ',
                contact_name_to_del, contact_email_to_del, 'не найдена',
                f"{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}Отмена удаления{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Ошибка запроса удаления{bcolors.ENDC}")
        
        
def export_contacts() -> None:
    
    ''' Экспорт контактов в Excel-файл
    Функция является оберткой для функции select_all_contacts_for_export,
    предназначенная для задания имени для файла'''
    
    file_name = input('Как назвать файл? ')
    export_file = select_all_contacts_for_export(file_name=file_name)
    if export_file:
        print(f"{bcolors.OKGREEN}Экспорт контактов прошел успешно!{bcolors.ENDC}")
    else:
       print(f"{bcolors.FAIL}Ошибка во время экспорта контактов!{bcolors.ENDC}") 
    