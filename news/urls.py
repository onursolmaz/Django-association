from django.urls import path, include
import home
from . import views
from django.shortcuts import redirect
urlpatterns = [

    path("", views.index, name="index"),
    path("<int:id>/<slug:slug>", views.news, name="news"),
    path("addcomment/<int:id>", views.addcomment, name="addcomment")

]