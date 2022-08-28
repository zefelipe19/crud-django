from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade')
    list_display_links = ('id', 'nome')
    

admin.site.register(Contact, ContactAdmin)