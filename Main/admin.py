from django.contrib import admin
from .models.Links import Link


# Register your models here.

# class AdminLink(admin.ModelAdmin):
#     list_display = ['video_link']



admin.site.register(Link)

