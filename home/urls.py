from django.urls import path,include
from . import views
from home.dash_apps.finished_apps import profplotly
from home.dash_apps.finished_apps import gesis


urlpatterns=[
    path('',views.home,name='home'),
    path('gesis.html',views.gesis,name='gesis'),
]