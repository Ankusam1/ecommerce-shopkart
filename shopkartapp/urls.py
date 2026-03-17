from django.urls import path
from shopkartapp import views
from django.contrib.auth import logout

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:id>/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='orders'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:id>/', views.add_wishlist, name='add_wishlist'),
    path('review/<int:id>/', views.add_review, name='add_review'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),



]
