from django.conf.urls import patterns, url
from estacionamientos import views

urlpatterns = patterns('',
    url(r'^estacionamientos/', views.EstacionamientosView.as_view()),
    url(r'^estacionamientos/?P<_id>\d+', views.EstacionamientoView.as_view()),
)
