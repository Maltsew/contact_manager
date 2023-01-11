# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:07:19 2022

@author: n.maltsev
"""


import argparse

def parse_command_line():
    parser = argparse.ArgumentParser(description='----------------------Телефонная книга----------------------')
    parser.add_argument(
        '-a',
        '--add_contact',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='-------------------------------------------------\
        Добавляет новый контакт в телефонную книгу \
            ___________________________________________________'
    )
    parser.add_argument(
        '-ls',
        '--show_contacts',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='-------------------------------------------------\
        Показывает все контакты телефонной книге \
            ___________________________________________________'
    )
    parser.add_argument(
        '-find',
        '--find_contact',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='-------------------------------------------------\
        Позволяет найти информацию о контакте. \
            ____ВНИМАНИЕ!____ \
         Поиск чувствителен к регистру! \
            ___________________________________________________'
    )
    parser.add_argument(
        '-rm',
        '--remove_contact',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='-------------------------------------------------\
        Удаляет контакт из телефонной книги \
            ___________________________________________________'
    )
    parser.add_argument(
        '-export',
        '--export_contact',
        nargs='?',
        const='',
        type=str,
        default=None,
        help='-------------------------------------------------\
        Экспорт контактов в Excel (.xlsx) \
            ___________________________________________________'
    )
    # parser.add_argument(
    #     '-change',
    #     '--change_database',
    #     nargs='?',
    #     const='',
    #     type=str,
    #     default=None,
    #     help='-------------------------------------------------\
    #     Выбор базы данных для хранения контактов \
    #         ___________________________________________________'
    # )
    # parser.add_argument(
    #     '-create_db',
    #     '--create_database',
    #     nargs='?',
    #     const='',
    #     type=str,
    #     default=None,
    #     help='-------------------------------------------------\
    #     Создание новой базы данных для хранения контактов \
    #         ___________________________________________________'
    # )
    my_namespace = parser.parse_args()
    return my_namespace
