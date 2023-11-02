from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('index2',views.index2, name='index2'),
    path('admin_home',views.admin_home, name='admin_home'),
    path('about',views.about, name='about'),
    path('login',views.login, name='login'),
    path('counter', views.counter, name="counter")
]