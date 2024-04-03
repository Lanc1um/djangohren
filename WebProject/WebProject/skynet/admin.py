from django.contrib import admin
from .models import *
# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo','time_create', 'is_published' )
    list_display_links = ("id", "title")
    search_fields = ("id", "title", "content")
    list_editable = ("is_published", )
    list_filter = ("time_create", "is_published")
    
admin.site.register(Services, ServicesAdmin)