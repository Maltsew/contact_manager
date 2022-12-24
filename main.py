# -*- coding: utf-8 -*-
"""
@author: n.maltsev
"""

from DB_worker import *
from cl_parser import parse_command_line
from contacts_manager import add_contact, show_all_contacts, search_inquiry, delete_contact, export_contacts

if __name__ == '__main__':
    
    space = parse_command_line()
    
    if space.show_contacts == '':
        show_all_contacts()
    elif space.show_contacts == None:
        pass
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для показа списка всех контактов --> {space.show_contacts}")
        
    if space.add_user == '':
        add_contact()
    elif space.add_user == None:
        pass
    else:
        print("Ошибка!")
        print(f"Недопустимый ввод для добавления нового контакта --> {space.add_user}")
        # print('Ошибка! Неправильный формат ввода')
        # print('Пожалуйста, дополните информацию о контакте \
        #                     или обратитесь за справкой указав команду -h')
        
    if space.find_contact == '':
        search_inquiry()
    elif space.find_contact == None:
        pass
    else:
        print("!Ошибка!")
        
    if space.remove_contact == '':
        delete_contact()
    elif space.remove_contact == None:
        pass
    else:
        print("!Ошибка!")
        
    if space.export_contact == '':
        export_contacts()
    elif space.remove_contact == None:
        pass
    else:
        print("!Ошибка!")

    if space.change_database == '':
        export_contacts()
    elif space.remove_contact == None:
        pass
    else:
        print("!Ошибка!")
        
        