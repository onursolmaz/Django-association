from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.views import category_news
from news.models import Category, News, Images


def index(request):
    return HttpResponse("News page")


def news(request, id):
    category = Category.objects.all()
    news = News.objects.get(pk=id)
    images = Images.objects.filter(news_id=id)
    context = {"news": news, "category": category, "images": images}
    return render(request, "news_detail.html", context)
