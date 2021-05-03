from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
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
    slug = models.SlugField()
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


class News(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # relation with Category
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=70)
    image = models.ImageField(blank=True, upload_to="images/")
    status = models.CharField(max_length=10, choices=STATUS)
    detail = RichTextUploadingField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = "Image"


class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return self.title
