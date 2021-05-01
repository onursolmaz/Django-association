from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


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


class ContactForm(models.Model):
    STATUS = (
        ("New", "New"),
        ("Read", "Read"),
    )

    name = models.CharField(max_length=75, blank=True)
    subject = models.CharField(blank=True, max_length=30)
    ip = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=30)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    message = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
