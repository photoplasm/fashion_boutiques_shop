from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm  # ตรวจสอบว่า UserProfileForm ใช้สำหรับ User Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from products.models import Product
from django.contrib.auth import views as auth_views

def home(request):
    products = Product.objects.all()  # ดึงสินค้าทั้งหมดจากฐานข้อมูล
    return render(request, 'home.html', {'products': products})

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username นี้ซ้ำ')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email นี้ซ้ำ')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return redirect('signup')

def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)  # ใช้ instance=request.user เพื่ออัพเดตข้อมูลใน User model
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/')  # Redirect ไปยังหน้า home หลังจากบันทึกสำเร็จ
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=request.user)  # โหลดข้อมูลปัจจุบันของผู้ใช้เพื่อแสดงในฟอร์ม
    return render(request, 'profile.html', {'form': form})


    