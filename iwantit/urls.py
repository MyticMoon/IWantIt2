__author__ = 'Hiep'
from django.conf.urls import patterns, url

from iwantit import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^searchitem/', views.searchitem, name='searchitem'),
    url(r'^shareit/', views.shareItAction, name='shareit'),
    url(r'^additem/', views.addItemAction, name='additem'),
    url(r'^vault/', views.vault, name='vault'),
    url(r'^pickitem/', views.pickitem, name='contact'),
    url(r'^loginView/', views.loginView, name='loginView'),
    url(r'^login', views.loginAction, name='login'),
    url(r'^logout/', views.logout, name='logout')
)