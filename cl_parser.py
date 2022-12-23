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
        default=None,
        help='---------------------------------------------\
        Добавляет новый контакт в телефонную книгу \
            _____________________________________________'
    )
    parser.add_argument(
        '-ls',
        '--show_contacts',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='---------------------------------------------\
        Показывает все контакты телефонной книге \
            _____________________________________________'
    )
    parser.add_argument(
        '-find',
        '--find_contact',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='---------------------------------------------\
        Позволяет найти информацию о контакте. \
        ВНИМАНИЕ! Поиск чувствителен к регистру! \
            _____________________________________________'
    )
    my_namespace = parser.parse_args()
    return my_namespace
