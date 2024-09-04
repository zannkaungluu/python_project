from django.contrib import admin
from shop.models import Category, Post, Content, Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'category', 'created_at']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'content']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'name', 'email', 'address', 'order_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Order, OrderAdmin)