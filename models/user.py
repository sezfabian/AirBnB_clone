#!/usr/bin/python3
'''User Class Definitive Module'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Initiallize User Class with attributes'''
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
