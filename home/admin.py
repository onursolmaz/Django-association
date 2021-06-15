from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "status", "answer"]
    list_filter = ["status"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user_name", "image_tag"]


admin.site.register(Setting)
admin.site.register(ContactFormMessage, ContactFormAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
