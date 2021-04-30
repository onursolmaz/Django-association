from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=75, blank=True)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=30)
    aboutus = models.TextField()
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
