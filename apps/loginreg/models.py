from __future__ import unicode_literals
from django.db import models

import bcrypt
import re


class UserManager(models.Manager):
    def register(self, reg_data):
        first_name = reg_data['first_name']
        last_name = reg_data['last_name']
        email = reg_data['email']
        birthday = reg_data['birthday']
        username = reg_data['username']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(email=email)
        except:
            user = False
        if len(first_name) >1 and len(first_name) >1 and len(username) >2 and len(password) >7 and password == confirm_password and not user:
        # still need to create our checks for birthday. maybe set up to have person be required to be 18
            u = self.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, username=username, password=hashed)
            print u
            print reg_data
            return (True,u)
        return (False,"Try again using only letters in name and username and double check your password")

    def login(self, log_data):
        email = log_data['email']
        user = self.filter(email=email)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or username are incorrect')



class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=150)
    birthday = models.DateField()
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
