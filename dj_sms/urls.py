# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'dj_sms'
urlpatterns = [
    path('', views.index),
    ]
