import json

from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, singUpForm
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


def category_news(request, id, slug):
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


def news_search_auto(request):
    if request.is_ajax():
        q = request.GET.get("term", "")
        news = News.objects.filter(title__icontains=q)
        results = []
        for rs in news:
            news_json = {}
            news_json = rs.title
            results.append(news_json)
        data = json.dumps(results)
    else:
        data = "fail"
    mimetype = "application/json"
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            messages.warning(request, "Username or Password incorrect !!!")
            return HttpResponseRedirect("/login")

    category = Category.objects.all()
    context = {"category": category}

    return render(request, "login.html", context)


def register_view(request):
    if request.method == 'POST':
        form = singUpForm(request.POST)
        if form.is_valid():
            form.username = request.POST["username"]
            form.email = request.POST["email"]
            form.first_name = request.POST["first_name"]
            form.last_name = request.POST["last_name"]
            form.password1 = request.POST["password1"]
            form.password2 = request.POST["password2"]
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")

    form = singUpForm()
    category = Category.objects.all()
    context = {"category": category, "form": form}
    return render(request, "register.html", context)
