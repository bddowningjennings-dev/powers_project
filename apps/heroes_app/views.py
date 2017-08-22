# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Hero, Power
from django.shortcuts import render, redirect
from django.contrib import messages

def heroes(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')
  none_powers = Power.objects.filter(name='None')
  context = {
    'users': User.objects.all(),
    'user': User.objects.get(id=request.session['user_id']),
    # 'heroes': none_powers,
    'heroes': Hero.objects.all(),
    'powers': Power.objects.all(),
  }
  return render(request, 'heroes_app/heroes.html', context)

def new_hero(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')    
  context = {
    'users': User.objects.all(),
    'user': User.objects.get(id=request.session['user_id']),
  }
  return render(request, 'heroes_app/new_hero.html', context)

def create_hero(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')
  results = Hero.objects.create_hero(request.POST)
  if len(results['errors']) > 0:
    for error in results['errors']:
      messages.error(request, error)
    return redirect('/heroes/new_hero')
  hero = Hero()
  hero.name = request.POST['name']
  hero.save()
  return redirect('/heroes')

def new_power(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')    
  context = {
    'users': User.objects.all(),
    'user': User.objects.get(id=request.session['user_id']),
  }
  return render(request, 'heroes_app/new_power.html', context)

def create_power(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')
  results = Power.objects.create_power(request.POST)
  if len(results['errors']) > 0:
    for error in results['errors']:
      messages.error(request, error)
    return redirect('/heroes/new_power')
  power = Power()
  power.name = request.POST['name']
  power.description = request.POST['description']
  power.save()
  return redirect('/heroes')

def add_power(request):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register') 
  hero = Hero.objects.get(id=request.POST['hero_id'])
  power = Power.objects.get(id=request.POST['power'])
  hero.powers.add(power)
  if request.POST['checkbox']:
    return redirect('/heroes/hero/{}'.format(request.POST['hero_id']))
  return redirect('/heroes')

def hero_show(request, hero_id):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register') 
  context = {
    'hero':  Hero.objects.get(id=hero_id),
    'powers': Power.objects.all(),
  }
  return render(request, 'heroes_app/hero_show.html', context)

def unlike(request, hero_id):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register')
  user = User.objects.get(id=request.session['user_id'])
  hero = Hero.objects.get(id=hero_id)
  hero.user_likes.remove(user)
  return redirect('/heroes')

def like(request, hero_id):
  try:
    request.session['user_id']
  except:
    return redirect('/register')
  if request.session['user_id'] == None:
    return redirect('/register') 
  user = User.objects.get(id=request.session['user_id'])
  hero = Hero.objects.get(id=hero_id)
  hero.user_likes.add(user)
  return redirect('/heroes')