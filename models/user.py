#!/usr/bin/python3
''' creates a user from the basemodel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Class implementation'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
