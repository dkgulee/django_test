from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('1', views.hello_world, name='hello_world'),
    path('chee', views.chee, name='hello_world'),
    path('nowtime', views.crrunt_datetime, name="current_time")

]
