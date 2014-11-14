# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

# Este error es raro, en django funciona
from estacionamientos import views

urlpatterns = patterns('',
    url(r'^$', views.estacionamientos_all, name='estacionamientos_all'),
    url(r'^(?P<_id>\d+)/$', views.estacionamiento_detail, name='estacionamiento_detail'),
    url(r'^(?P<_id>\d+)/reserva$', views.estacionamiento_reserva, name='estacionamiento_reserva'),
)
