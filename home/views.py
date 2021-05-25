from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactFormMessage, ContactForm
from django.contrib import messages

from news.models import News, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderData = News.objects.all()[:4]
    category = Category.objects.all()
    news = News.objects.all()
    context = {"setting": setting, "sliderData": sliderData, "category": category, "news": news}
    return render(request, "index.html", context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {"setting": setting, "category": category}
    return render(request, "news.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data["name"]
            data.email = form.cleaned_data["email"]
            data.phone = form.cleaned_data["phone"]
            data.message = form.cleaned_data["message"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            messages.success(request, "Your message has been sent successfully")
            return HttpResponseRedirect("/contact")

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    # form = ContactForm()
    context = {"setting": setting, "category": category}
    return render(request, "contact.html", context)


def category_news(request, id):
    category = Category.objects.all()
    categoryData = Category.objects.get(pk=id)
    news = News.objects.filter(category_id=id)
    context = {"news": news, "category": category, "categoryData": categoryData}
    return render(request, "news.html", context)


def news_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data["query"]
            news = News.objects.filter(title__icontains=query)
            context = {"news": news, "category": category}
            return render(request, "news_search.html", context)

    return HttpResponseRedirect("/")
