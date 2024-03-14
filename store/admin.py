from django.contrib import admin
from django.utils.html import format_html


from .models import CartItem, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image_display')

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return 'No image'
    image_display.short_description = 'Image'

admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, )
