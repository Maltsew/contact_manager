# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:16:21 2022

@author: n.maltsev
"""


from cl_parser import parse_command_line
from DB_worker import *
from contact_validators import *
from bcolors import bcolors



def validate_contact():
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

    
def add_contact():
    if validate_contact():
        contact_name, contact_email, contact_phone = data
        add_contact_to_table(contact_name=contact_name,
                             contact_email=contact_email,
                             contact_phone=contact_phone)
        #print('Контакт добавлен!')
        print(f"{bcolors.OKGREEN}Контакт добавлен!{bcolors.ENDC}")
    
    
def show_all_contacts():
    all_contacts_info = select_all_contacts()
    return all_contacts_info


def contact_info_insertion():
    input_name = input('Введите ФИО: ')
    input_email = input('Введите адрес электронной почты: ')
    input_phone = input('Введите номер телефона:')
    global data
    data = (input_name, input_email, input_phone)
    return input_name, input_email, input_phone

def search_inquiry():
    ''' Поисковой запрос - информация от пользователя о контакте (Данные о ФИО,
    почте либо телефоне'''
    search_info = input('Введите информацию о контакте: ')
    #print('                  Результат поиска: ')
    print(f"{bcolors.OKCYAN}                  Результат поиска:{bcolors.ENDC}")
    if search_info != '':
        contact_search_query(contact_info=search_info)
    else:
        #print('Пустой поисковой запрос!')
        print(f"{bcolors.FAIL}Пустой поисковой запрос!{bcolors.ENDC}")
    
def delete_contact():
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
        
        
def export_contacts():
    file_name = input('Как назвать файл? ')
    export_file = select_all_contacts_for_export(file_name=file_name)
    if export_file:
        print(f"{bcolors.OKGREEN}Экспорт контактов прошел успешно!{bcolors.ENDC}")
    else:
       print(f"{bcolors.FAIL}Ошибка во время экспорта контактов!{bcolors.ENDC}") 
    