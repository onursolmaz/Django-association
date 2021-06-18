from django.urls import path, include
import home
from . import views
from django.shortcuts import redirect

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:id>/<slug:slug>", views.news, name="news"),
    path("addcomment/<int:id>", views.addcomment, name="addcomment"),
    path("delete/<int:id>", views.delete_news, name="delete_news"),
    path("delete_comment/<int:id>", views.delete_comment, name="delete_comment"),
    path("add_news", views.add_news, name="add_news"),
    # path("edit_news/<int:id>", views.edit_news, name="edit_news"),

]
