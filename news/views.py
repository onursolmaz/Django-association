from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.views import category_news
from news.models import Category, News, Images, CommentForm, Comment


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


def delete_comment(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    messages.success(request, "news has been deleted")
    return HttpResponseRedirect("/user/mynews")
