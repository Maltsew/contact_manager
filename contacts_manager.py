# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:16:21 2022

@author: n.maltsev
"""


from cl_parser import parse_command_line

def add_user():
        f = parse_command_line()
        if f.add_user is not None:
            if f.add_user != '':
                new_user = f.add_user.split(" ")
                print(new_user)
                if len(new_user) == 3:
                    print('<--Добавлен новый контакт-->')
                    print('ФИО', new_user[0], '|',
                          'Адрес электронной почты', new_user[1], '|',
                          'Номер телефона', new_user[2], '|')
                else:
                    print('Ошибка! Неправильный формат ввода')
            else:
                print('Новый контакт не может быть пустым. Пожалуйста, \
                      дополните информацию о контакте \
                          или обратитесь за справкой указав команду -h')
        return 1
    
def show_contacts():
        f = parse_command_line()
        all_contacts = f.show_contacts
        print(all_contacts)
        return 1