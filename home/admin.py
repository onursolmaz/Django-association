from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message","status","answer"]
    list_filter = ["status"]


admin.site.register(Setting)

admin.site.register(ContactFormMessage,ContactFormAdmin)
