from django.contrib import admin
from .models import profile


class Profile(admin.ModelAdmin):
   list_display = ('id', 'store_name', 'professional_email', 'birth_date')
   list_display_links = ('id', 'store_name', 'professional_email', 'birth_date')
   
  
admin.site.register(profile, Profile)
