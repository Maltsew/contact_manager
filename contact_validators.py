# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:21:07 2022

@author: n.maltsev
"""


import re


def contact_name_is_cyrrilic(text):
    return bool(re.match('[(а-яА-Я) + \s + \-]', text))
    #return bool(re.fullmatch('?:[А-Я](?:\.|[а-я]+)', text))

def contact_email_is_valid(email):
    return bool(re.fullmatch(
        '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email))

def contact_phone_is_valid(phone):
    #return bool(re.fullmatch("8(?:-\\d{3}){2}(?:-\\d{2}){2}", phone))
    return bool(re.fullmatch("8", phone))