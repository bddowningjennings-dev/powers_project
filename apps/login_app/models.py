# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class UserManager(models.Manager):
  def validate_register(self, postData):
    results = {
      'errors': [],
    }
    for data in postData:
      if str(data) != 'email':
        if len(postData[data]) < 3 and str(data) != 'c_password' and str(data) != 'password':
          results['errors'].append('{} field must at least 3 characters long'.format(' '.join(data.split('_')).capitalize()))
        if len(postData[data]) < 8 and str(data) == 'password':
          results['errors'].append('{} field must at least 8 characters long'.format(data.capitalize()))
      elif not re.match(EMAIL_REGEX, postData['email']):
        results['errors'].append('Invalid Email')
      elif User.objects.filter(email=postData['email']).count() > 0:
          results['errors'].append('Email already registered')
    if postData['password'] != postData['c_password']:
        results['errors'].append('Password confirmation error')        
    return results

  def add(self, postData):
    user = User()
    user.name = postData['name'].capitalize()
    user.email = postData['email']
    hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
    user.password = hashed
    user.save()
    return user

  def validation_login(self, postData):
    results = {
      'errors': [],
    }
    for data in postData:
      if len(postData[data]) < 1 and str(data) != 'c_password':
        results['errors'].append('{} field may not be blank'.format(data.capitalize()))
    if User.objects.filter(email=postData['email']).count() < 1:
        results['errors'].append('Email/Password not currently registered')
    else:
      hashed_pw = User.objects.filter(email=postData['email'])[0].password
      if not bcrypt.checkpw(postData['password'].encode(), hashed_pw.encode()):
        results['errors'].append('Email/Password not valid')        
    return results

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  password = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  objects = UserManager()
  def __str__(self):
    return '\nUser:\nname: {}\nemail: {}\n'.format(self.name, self.email)
