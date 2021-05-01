from django.contrib import admin

# Register your models here.
from news.models import Category, News, Images


class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status", "image_tag"]
    list_filter = ["status"]
    inlines = [NewsImageInline]
    readonly_fields = ("image_tag",)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title", "news", "image"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)
