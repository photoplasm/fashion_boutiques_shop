from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Review, Wishlist
from .forms import ProductForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser

# Create Product (Admin Only)
@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # เปลี่ยนเส้นทางหลังจากบันทึก
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})
def product_list(request):
    products = Product.objects.all()  # หรือคุณสามารถทำการจัดการ pagination ที่นี่ได้
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # รับข้อมูลสินค้า
    return render(request, 'product_detail.html', {'product': product})
# View for listing products with pagination and search functionality
def products(request):
    query = request.GET.get('q')  # รับคำค้นหาจาก URL
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(material__icontains=query)
        ).distinct()  # เพิ่ม distinct เพื่อหลีกเลี่ยงผลลัพธ์ที่ซ้ำกัน

    paginator = Paginator(products, 6)  # Paginate products, 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj, 'query': query})

    return render(request, 'products.html', {'page_obj': page_obj, 'query': query})

# Add Product to Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    product_price = float(product.price)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': product_price,
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('products')

# Remove Product from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('cart')

# View Cart
def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

# Update Cart
def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] = quantity
            request.session['cart'] = cart
    return redirect('cart')

# Checkout
def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item in cart.values():
        item_total = item['price'] * item['quantity']
        total_price += item_total
        cart_items.append({
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'total': item_total,
        })

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# Complete Checkout
def complete_checkout(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment_method')

        # Handle the payment and order logic here
        # เช่น บันทึกข้อมูลคำสั่งซื้อในฐานข้อมูล

        try:
            send_mail(
                'Order Confirmation',
                f'Thank you for your order, {full_name}. We will ship your items to {address}.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, "Your order has been placed successfully!")
        except Exception as e:
            messages.error(request, "There was an error sending the confirmation email. Please try again later.")

        # Clear the cart after successful checkout
        request.session['cart'] = {}

        return redirect('order_confirmation')

    # If the request method is not POST, redirect to cart
    messages.warning(request, "Invalid request method.")
    return redirect('cart')

# Order Confirmation
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def add_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST['rating']
        comment = request.POST['comment']
        
        Review.objects.create(product=product, rating=rating, comment=comment)
        
        return redirect('product_detail', product_id=product.id)
    
# Edit Product (Admin Only)
@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form, 'product': product})




# Delete Product (Admin Only)
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")

@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist_detail')

@login_required
def wishlist_detail(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist_detail.html', {'wishlist': wishlist})

def remove_from_wishlist(request, product_id):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    wishlist.products.remove(product)  # ลบสินค้าออกจากรายการโปรด
    return redirect('wishlist_detail')  # กลับไปยังหน้ารายการโปรด
