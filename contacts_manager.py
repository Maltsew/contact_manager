# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:16:21 2022

@author: n.maltsev
"""


from cl_parser import parse_command_line
from DB_worker import add_contact_to_table
from contact_validators import contact_name_is_cyrrilic, contact_email_is_valid, contact_phone_is_valid



def validate_contact():
    try:
        print('Вызов в валидации')
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


# def validate_contact():
#     f = parse_command_line()
#     if f.add_user == '':
#         print('!!!')
#         try:
#             new_contact_name, new_contact_email, new_contact_phone = contact_info_insertion()
#             if contact_name_is_cyrrilic(new_contact_name):
#                 if contact_email_is_valid(new_contact_email):
#                     if contact_phone_is_valid(new_contact_phone):
#                         return True
#                     else:
#                         print('Номер телефона введен неверно')
#                 else:
#                     print('Адрес почты введен неверно')
#             else:
#                 print('Имя введено неверно')
#         except TypeError:
#             print('!!!')
#     else:
#        print('Ошибка! Неправильный формат ввода')
#        print('Пожалуйста, дополните информацию о контакте \
#                             или обратитесь за справкой указав команду -h')
#     return False

    
def add_contact():
    if validate_contact():
        print('вызов в добавлении')
        contact_name, contact_email, contact_phone = data
        add_contact_to_table(contact_name=contact_name,
                             contact_email=contact_email,
                             contact_phone=contact_phone)
    
    
def show_contacts():
        f = parse_command_line()
        all_contacts = f.show_contacts
        print(all_contacts)
        return 1


def contact_info_insertion():
    print('Введите ФИО')
    input_name = input()
    print('Введите адрес электронной почты')
    input_email = input()
    print('Введите номер телефона')
    input_phone = input()
    global data
    data = (input_name, input_email, input_phone)
    return input_name, input_email, input_phone

    