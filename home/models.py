from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import Textarea, TextInput, NumberInput, ModelForm


class Setting(models.Model):
    title = models.CharField(max_length=75, blank=True)
    keywords = models.CharField(max_length=200)
    description = RichTextUploadingField()
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=30)
    aboutus = RichTextUploadingField()
    smtpserver = models.CharField(blank=True, max_length=16)
    smtpemail = models.CharField(blank=True, max_length=30)
    smtppassword = models.CharField(blank=True, max_length=15)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to="images/")
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    linkedin = models.CharField(blank=True, max_length=100)
    youtube = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ("New", "New"),
        ("Read", "Read"),
        ("Closed", "Closed"),
    )

    name = models.CharField(max_length=75, blank=True)
    email = models.CharField(blank=True, max_length=30)
    phone = models.CharField(blank=True, max_length=15)
    ip = models.CharField(blank=True, max_length=20)
    message = models.CharField(max_length=255)
    answer = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": TextInput(attrs={"class": "input", "placeholder": "Please enter Name Surname"}),
            "email": TextInput(attrs={"class": "input", "placeholder": "Please enter email"}),
            "phone": NumberInput(attrs={"class": "input", "placeholder": "Your phone"}),
            "message": Textarea(attrs={"class": "input", "placeholder": "Please enter Name Surname"})
        }


