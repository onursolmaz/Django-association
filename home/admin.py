from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "status"]
    list_filter = ["status"]


admin.site.register(Setting)
admin.site.register(ContactForm)
