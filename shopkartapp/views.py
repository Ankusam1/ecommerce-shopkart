from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from shopkartapp.models import Product,CartItem,Order,OrderItem,Wishlist,Review,Category
from django.db.models import Q
from django.shortcuts import get_object_or_404




# Create your views here.


def home(request):

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    # Search filter
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # Category filter
    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })

@login_required
def add_to_cart(request,id):

    product = Product.objects.get(id=id)

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)

    total = 0
    for i in items:
        total += i.product.price * i.quantity

    return render(request,'cart.html',{
        'items':items,
        'total':total
    })

@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)

    total = sum(i.product.price * i.quantity for i in items)

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for i in items:
        OrderItem.objects.create(
            order=order,
            product=i.product,
            quantity=i.quantity,
            price=i.product.price
        )

    items.delete()

    return redirect('orders')

@login_required
def order_history(request):
    orders=Order.objects.filter(user=request.user)
    return render(request,'orders.html',{'orders':orders})

@login_required
def add_wishlist(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('home')

@login_required
def wishlist_view(request):
    items=Wishlist.objects.filter(user=request.user)
    return render(request,'wishlist.html',{'items':items})

@login_required
def add_review(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        Review.objects.create(
            user=request.user,
            product=product,
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
    return redirect('home')

@login_required
def product_detail(request,id):

    product = Product.objects.get(id=id)

    return render(request,'product_detail.html',{
        'product':product
    })

def register(request):
    if request.method=="POST":
        user=User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request,user)
        return redirect('home')
    return render(request,'register.html')

@login_required
def profile(request):
    return render(request,'profile.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def remove_cart(request,id):
    item = CartItem.objects.get(id=id)
    item.delete()
    return redirect('cart')



