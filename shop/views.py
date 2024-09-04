from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def drink(request):
    category = request.GET.get('category')
    search = request.GET.get('search')
    if search:
        page_obj = Post.objects.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        )
    else:      
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'drink.html',{'posts':page_obj})


        

def about(request):
    return render (request, 'about.html')

def content(request):
    if request.method == "GET":
        content = Content.objects.all()
        return render(request, 'content.html',{'content':content})
    if request.method == "POST":
        Content.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            content = request.POST.get('content')
        )
        return redirect('/content')


@permission_required('shop.add_post', login_url='login')
def create(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, 'create.html',{'category':category})
    if request.method == "POST":
        Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            image = request.FILES.get('image'),
            category_id = request.POST.get('category'),
            author_id = request.user.id
        )
    messages.success(request, "Post Created Success!")
    return redirect('/create')

@permission_required('shop.detail_post', login_url='login')
def detail(request, p_id):
    if request.method == "GET":
        post = Post.objects.get(id=p_id)
        return render(request, 'detail.html', {'p':post})
    if request.method == "POST":
        return redirect(f'/detail/{p_id}')
    
@permission_required('shop.delete_post', login_url='login')
def delete(request, p_id):
    post = Post.objects.get(id=p_id)
    post.image.delete()
    post.delete()
    messages.error(request, "Post Deleted Success!")
    return redirect('/drink')

def LOGIN(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success!")
            return redirect('/drink')
        else:
            messages.error(request, "Username or Password is Incorrect!")
            return redirect('/login')
        
def LOGOUT(request):
    logout(request)
    return redirect ('/drink')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password == repassword:
            if User.objects.filter(username=username):
                messages.error(request, 'username already exists')
                return redirect('/register')
            if User.objects.filter(email=email):
                messages.error(request, 'email already exists')
                return redirect('/register')
            User.objects.create(
                username = username,
                email = email,
                password = make_password(password)
            )
            return redirect('/login')
        else:
            messages.error(request, 'password are not same')
            return redirect('/register')

def order(request, p_id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=p_id)
        return render(request, 'order.html', {'p': post})
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        o = Order(
            title = title,
            content = content,
            name=name,
            email=email,
            address=address
        )
        o.save()
        messages.success(request, "Order is successful!")
        return redirect(f'/order/{p_id}')

def pagenotfound(request):
    return render(request, '404.html')   