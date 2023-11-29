from django.contrib import admin
from .models import product, message, bag, comment


admin.site.register(product)
admin.site.register(message)
admin.site.register(bag)


class comments(admin.ModelAdmin):
    list_display = ('user', 'product', 'message', 'created_at')
    list_display_links = ('user', 'created_at')

admin.site.register(comment, comments)