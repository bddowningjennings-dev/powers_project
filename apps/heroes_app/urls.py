"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new_power$', views.new_power),
    url(r'hero/(?P<hero_id>\w+)$', views.hero_show),
    url(r'unlike/(?P<hero_id>\w+)$', views.unlike),
    url(r'like/(?P<hero_id>\w+)$', views.like),
    url(r'add_power$', views.add_power),
    url(r'new_hero$', views.new_hero),
    url(r'create_hero$', views.create_hero),
    url(r'create_power$', views.create_power),
    url(r'^', views.heroes),
]