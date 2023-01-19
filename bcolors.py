# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:05:15 2023

@author: n.maltsev

Модуль содержит класс переменных для задания цвета тексту вывода сообщений
при работе приложения
"""


class bcolors:
    HEADER = '\033[95m' #1
    OKBLUE = '\033[94m' #2
    OKCYAN = '\033[96m' #3
    OKGREEN = '\033[92m' #4
    WARNING = '\033[93m' #5 желтый
    FAIL = '\033[91m' #6 красный
    ENDC = '\033[0m' #7
    BOLD = '\033[1m' #8
    UNDERLINE = '\033[4m' #9