from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from news.models import Category, News, Images


class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(MPTTModelAdmin):
    list_display = ["title", "status"]
    list_filter = ["status"]


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status", "image_tag"]
    list_filter = ["status"]
    inlines = [NewsImageInline]
    readonly_fields = ("image_tag",)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ["title", "news", "image"]




class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                News,
                'category',
                'news_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 News,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Releted News Count'

    def related_products_cumulative_count(self, instance):
        return instance.news_cumulative_count
    related_products_cumulative_count.short_description = 'Sub Related News Count'



admin.site.register(Category, CategoryAdmin2)
admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)
