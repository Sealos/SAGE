from django.conf.urls import patterns, url
from estacionamiento import views

urlpatterns = patterns('',
    url(r'^estacionamiento/', views.EstacionamientosView.as_view()),
    url(r'^estacionamiento/?P<_id>\d+', views.EstacionamientoView.as_view()),
)
