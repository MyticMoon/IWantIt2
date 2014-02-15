__author__ = 'Hiep'
from django.conf.urls import patterns, url

from iwantit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^searchitem/', views.searchitem, name='contact'),
    url(r'^shareit/', views.shareItAction, name='contact')
)