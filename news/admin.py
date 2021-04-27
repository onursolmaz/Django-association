from django.contrib import admin

# Register your models here.
from news.models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status"]
    list_filter = ["status"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
