from django.urls import path
from . import views

#creating url patterns...
urlpatterns =[
    path('welcome/',views.welcome,name='wel')
]