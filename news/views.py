from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.views import category_news
from news.models import Category, News, Images, CommentForm, Comment, NewsForm


def index(request):
    return HttpResponse("News page")


def news(request, id, slug):
    category = Category.objects.all()
    news = News.objects.get(pk=id)
    images = Images.objects.filter(news_id=id)
    comments = Comment.objects.filter(news_id=id, status="True")
    context = {"news": news, "category": category, "images": images, "comments": comments}
    return render(request, "news_detail.html", context)


@login_required(login_url="/login")
def addcomment(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.news_id = id
            data.comment = form.cleaned_data["comment"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            messages.success(request, "Comment has been sent")

            return HttpResponseRedirect(url)

    messages.error(request, "Comment can not sent")
    return HttpResponse(url)


@login_required(login_url="/login")
def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    messages.success(request, "news has been deleted")
    return HttpResponseRedirect("/user/mynews")


@login_required(login_url="/login")
def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    comment.delete()
    messages.success(request, "comment has been deleted")
    return HttpResponseRedirect("/user/mycomments")


@login_required(login_url="/login")
def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            news = News()
            news.title = form.cleaned_data["title"]
            news.category = form.cleaned_data['category']
            news.slug = form.cleaned_data["slug"]
            news.detail = form.cleaned_data["detail"]
            news.user_id = current_user.id
            news.image = form.cleaned_data["image"]
            news.keywords = form.cleaned_data["keywords"]
            news.save()
            messages.success(request, "News has been added")
            return HttpResponseRedirect("/user/mynews")
        else:
            messages.success(request, "News form error:" + str(form.errors))

    else:
        category = Category.objects.all()
        form = NewsForm()
        context = {"form": form, "category": category}
        return render(request, "user_addNews.html", context)


def add_newsTest(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            print("form verisi:")
            category = form.cleaned_data['category']
            print(category)
            print("verinin type**********************************************:")
            print(type(category))

            exit()
        else:
            print(str(form.errors))
            exit()
    else:
        category = Category.objects.all()
        form = NewsForm()
        context = {"form": form, "category": category}
        return render(request, "user_addNews.html", context)
