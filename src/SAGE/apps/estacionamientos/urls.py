# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

# Este error es raro, en django funciona
from apps.estacionamientos import views

urlpatterns = patterns('',
    url(r'^$', views.estacionamientos_all, name='estacionamientos_all'),
    url(r'^(?P<_id>\d+)/$', views.estacionamiento_detail, name='estacionamiento_detail'),
)
