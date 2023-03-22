from django.contrib import admin
from .models import Display
# Register your models here.
class DisplayAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    # list_filter = ['is_published']
    # search_fields = ['title']

admin.site.register(Display, DisplayAdmin)
# admin.site.register(AddToCart)
