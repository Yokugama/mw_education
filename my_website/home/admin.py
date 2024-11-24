from django.contrib import admin

# Register your models here.
from home.models import Settings
from home.models import ContactMessage

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'note', 'status']
    readonly_fields = ('name', 'phone', 'subject', 'message', 'ip')
    list_filter = ['status']

admin.site.register(Settings, SettingsAdmin)

admin.site.register(ContactMessage, ContactMessageAdmin)