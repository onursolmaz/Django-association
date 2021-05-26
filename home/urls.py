from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("aboutus", views.aboutus, name="abouts"),
    path("contact", views.contact, name="contact"),
    path("<int:id>/<slug:slug>", views.category_news, name="category_news"),

]
