from django.conf.urls import patterns, url

from apps.estacionamientos import views

urlpatterns = patterns('',
    url(r'^$', views.estacionamiento, name='estacionamiento'),
)