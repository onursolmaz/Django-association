from django.urls import path, include
import home
from . import views
from django.shortcuts import redirect
urlpatterns = [

    path("", views.index, name="index"),
    path("<int:id>", views.news, name="news"),

]