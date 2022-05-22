from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('groundbase',views.groundbase,name='groundbase'),
    path('football',views.football,name='football'),
    path('footballground1',views.footballg1,name='footballground1'),
    path('footballground2',views.footballg2,name='footballground2'),
    path('footballground3',views.footballg3,name='footballground3'),
    path('footballground4',views.footballg4,name='footballground4'),
    path('cricket',views.cricket,name='cricket'),
    path('cricketg1',views.cricketg1,name='cricketg1'),
    path('cricketg2',views.cricketg2,name='cricketg2'),
    path('cricketg3',views.cricketg3,name='cricketg3'),
    path('cricketg4',views.cricketg4,name='cricketg4'),
    # path('search_ground',views.search_ground,name='search-ground'),
]