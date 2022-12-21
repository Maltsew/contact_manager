# -*- coding: utf-8 -*-
"""
@author: n.maltsev
"""

from create_DB import *
from cl_parser import parse_command_line
from contacts_manager import add_user, show_contacts

if __name__ == '__main__':
    create_table_user()
    create_test_user()
    #drop_user_table()
    #create_test_user()
    #display_DB_info()
    #input_new_user()
    #add_user()
    #show_contacts()
    display_DB_info()
    