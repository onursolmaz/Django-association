from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, FileInput, Select
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )

    title = models.CharField(max_length=60)
    keywords = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to="images/")
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return "/".join(full_path[::-1])

    class MPTTMeta:
        order_insertion_by = ["title"]

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class News(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # relation with Category
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=70)
    image = models.ImageField(blank=True, upload_to="images/")
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    detail = RichTextUploadingField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = "Image"

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})


#
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["category", "title", "slug", "keywords", "detail", "image", ]
        widgets = {
            "category": Select(attrs={"class": "input form-control","name":"filter_by"}),
            "title": TextInput(attrs={"class": "input form-control", "placeholder": "title"}),
            "slug": TextInput(attrs={"class": "input form-control", "placeholder": "slug"}),
            "keywords": TextInput(attrs={"class": "input form-control", "placeholder": "keywords"}),
            "image": FileInput(attrs={"class": "input form-control", "placeholder": "image",}),
            "detail": CKEditorWidget(),
        }


class Comment(models.Model):
    STATUS = (
        ("New", "Yeni"),
        ("True", "Evet"),
        ("False", "Hayır"),

    )

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(blank=True, max_length=16)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]


class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return self.title
