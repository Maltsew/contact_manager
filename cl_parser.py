# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:07:19 2022

@author: n.maltsev
"""


import argparse

def parse_command_line():
    parser = argparse.ArgumentParser(description='Телефонная книга')
    parser.add_argument(
        '-a',
        '--add_user',
        nargs='?',
        const='',
        type=str,
        default='',
        help='Добавляет новый контакт в телефонную книгу. \
              Формат ввода данных <--Фамилия Имя Отчество \
              Адрес электронной почты Телефон-->\
              '
    )
    parser.add_argument(
        '-ls',
        '--show_contacts',
        type=str,
        default=None,
        help='Показывает все контакты телефонной книги'
    )
    my_namespace = parser.parse_args()
    return my_namespace
