# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models


class HeroManager(models.Manager):
  def create_hero(self, postData):
    results = {
      'errors': [],
    }
    if len(postData['name']) < 2:
      results['errors'].append('Hero names must be at least 2 characters')
    return results

class PowerManager(models.Manager):
  def create_power(self, postData):
    results = {
      'errors': [],
    }
    if len(postData['name']) < 1:
      results['errors'].append('Power names may not be blank')
    if len(postData['description']) < 1:
      results['errors'].append('Power descriptions may not be blank')
    return results

class Hero(models.Model):
  name = models.CharField(max_length=100)
  user_likes = models.ManyToManyField(User, related_name='heroes_likes')
  created_at = models.DateField(auto_now_add=True)
  objects = HeroManager()
  def __str__(self):
    return '\nHero:\nname: {}\npower(s): {}\n'.format(self.name, self.powers)

class Power(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  heroes = models.ManyToManyField(Hero, related_name='powers')
  created_at = models.DateField(auto_now_add=True)
  objects = PowerManager()
  def __str__(self):
    return '\nPower:\nname: {}\ndescription: {}\n'.format(self.name, self.description)

# class hero_power(models.Model):
#   power = models.ForeignKey(Power, related_name='heros')
#   hero = models.ForeignKey(Hero, related_name='powers')



