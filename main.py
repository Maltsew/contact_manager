# -*- coding: utf-8 -*-
"""
@author: n.maltsev
"""

import functools
from main_commands import *

if __name__ == '__main__':
    command_add_contact()
    command_show_contact()
    command_find_contact()
    command_remove_contact()
    command_export_contacts()
    #command_change_database()
    #command_create_database()
    


# def trackcalls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.has_been_called = True
#         return func(*args, **kwargs)
#     wrapper.has_been_called = False
#     return wrapper

# @trackcalls
# def example(a, b):
#     return a + b

# #example(1, 2)

# if example.has_been_called:
#     print('Уже вызвана')
# else:
#     print('Нужно вызвать example')