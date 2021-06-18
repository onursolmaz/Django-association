from django.urls import path
from . import views

urlpatterns = [

    path("profile", views.userProfile, name="userProfile"),
    path("update/", views.user_update, name="user_update"),
    path("password/", views.change_password, name="change_password"),
    path("mynews/", views.my_news, name="my_news"),
    path("mycomments/", views.my_comments, name="my_comments"),




]
