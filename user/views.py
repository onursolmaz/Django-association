from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile, Setting
from news.models import Category, News, Comment
from django.contrib import messages

from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url="/login")
def userProfile(request):
    category = Category.objects.all()
    user = request.user
    setting = Setting.objects.get(pk=1)
    profile = UserProfile.objects.get(user_id=user.id)
    context = {"category": category, "profile": profile, "user": user, "setting": setting}
    return render(request, "user_profile.html", context)

    return HttpResponse("User Page")


@login_required(login_url="/login")
def user_update(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "your account has been updated")
            return redirect("/user/profile")
    else:
        category = Category.objects.all()
        user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        setting = Setting.objects.get(pk=1)
        context = {"category": category, "user_form": user_form, "profile_form": profile_form, "user": user,
                   "setting": setting}
        return render(request, "user_update.html", context)


@login_required(login_url="/login")
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "your password has been updated")
            return HttpResponseRedirect("/user/profile")
        else:
            messages.warning(request, "Please correct the error blow <br>" + str(form.errors))
            return HttpResponseRedirect("/user/password")
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        setting = Setting.objects.get(pk=1)
        context = {"category": category, "form": form, "setting": setting}
        return render(request, "change_password.html", context)


def my_news(request):
    category = Category.objects.all()
    user = request.user
    news = News.objects.filter(user_id=user.id)
    setting = Setting.objects.get(pk=1)
    context = {"category": category, "news": news, "setting": setting}
    return render(request, "user_news.html", context)


def my_comments(request):
    category = Category.objects.all()
    user = request.user
    comments = Comment.objects.filter(user_id=user.id)
    setting = Setting.objects.get(pk=1)
    context = {"category": category, "comments": comments, "setting": setting}
    return render(request, "user_comments.html", context)
