from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile, FAQ


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "status", "answer"]
    list_filter = ["status"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user_name", "image_tag"]


admin.site.register(Setting)
admin.site.register(ContactFormMessage, ContactFormAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ["orderNumber", "question", "answer", "status"]
    list_filter = ["status"]

admin.site.register(FAQ, FAQAdmin)


