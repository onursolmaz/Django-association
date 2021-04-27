from django.db import models


# Create your models here.

class Category(models.Model):
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
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


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
    detail = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
