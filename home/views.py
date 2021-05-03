from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactForm
from django.contrib import messages

from news.models import News, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderData = News.objects.all()[:4]
    category = Category.objects.all()
    context = {"setting": setting, "sliderData": sliderData, "category": category}
    return render(request, "index.html", context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {"setting": setting,"category": category}
    return render(request, "aboutus.html", context)


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
    context = {"setting": setting,"category": category}
    return render(request, "contact.html", context)
