from django.contrib import admin
from shopkartapp.models import Category,Product,CartItem,Order,OrderItem,Wishlist,Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(Review)

