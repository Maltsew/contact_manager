# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:16:21 2022

@author: n.maltsev
"""


from cl_parser import parse_command_line
from DB_worker import add_contact_to_table, select_all_contacts, contact_search
from contact_validators import contact_name_is_cyrrilic, contact_email_is_valid, contact_phone_is_valid



def validate_contact():
    try:
        new_contact_name, new_contact_email, new_contact_phone = contact_info_insertion()
        if contact_name_is_cyrrilic(new_contact_name):
            if contact_email_is_valid(new_contact_email):
                if contact_phone_is_valid(new_contact_phone):
                    return True
                else:
                    print('Номер телефона введен неверно')
            else:
                print('Адрес почты введен неверно')
        else:
            print('Имя введено неверно')
    except TypeError:
        print('!!!')
    return False

    
def add_contact():
    if validate_contact():
        contact_name, contact_email, contact_phone = data
        add_contact_to_table(contact_name=contact_name,
                             contact_email=contact_email,
                             contact_phone=contact_phone)
        print('Контакт добавлен!')
    
    
def show_all_contacts():
    all_contacts_info = select_all_contacts()
    return all_contacts_info


# Перенести в интерфейсы
def contact_info_insertion():
    #print('Введите ФИО')
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
    print('                  Результат поиска: ')
    if search_info != '':
        contact_search(contact_info=search_info)
    else:
        print('Пустой поисковой запрос!')
    
    