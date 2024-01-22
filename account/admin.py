from django.contrib import admin
from .models import profile, reviews


class Profile(admin.ModelAdmin):
   list_display = ('id', 'store_name', 'professional_email')
   list_display_links = ('id', 'store_name', 'professional_email')
   
  
admin.site.register(profile, Profile)
admin.site.register(reviews)