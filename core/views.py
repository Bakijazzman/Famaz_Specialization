from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UserInfoForm
import json
from cart.cart import Cart


def update_profile(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Profile has been Updated"))
            return redirect("index")
        else:
            for err in list(form.errors.values()):
                messages.error(request, err)
            return render(request, 'update_profile.html', {"form":form})
    else:
        messages.success(request, ("You have to login first"))
        return redirect("login")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Password Successfully changed, please log in again"))
                return redirect("login")
            else:
                for err in list(form.errors.values()):
                    messages.error(request, err)
                return redirect("password")     
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, "update_password.html", {"form":form})
    else:
        messages.success(request, ("You have to login first"))
        return redirect("login")
    
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products':products})

def about(request):
    return render(request, 'about.html', {})

def category(request, foo):
    # replacing hyphen from the request with spaces
    foo = foo.replace('-', ' ')
    try:
        # look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(Category=category)
        return render(request, "category.html", {'products':products, 'category':category})
    except:
        messages.success(request,("That category doesnt exist"))
        return redirect("index")

# The login function
def login_user(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            current_user = Profile.objects.get(user__id=request.user.id)
            # load saved cart
            saved = current_user.old_cart
            # covert json
            if saved:
                converted = json.loads(saved)
                cart = Cart(request)
                # add items from database
                for k,v in converted.items():
                    cart.db_add(product=k, quantity=v)
                
            
            messages.success(request,("You have been logged in "))
            return redirect('index')
        else:
            messages.success(request,("There was an error please try again"))
            return redirect("login")
    else:
        return render(request, 'login.html', {})

# The logout function
def logout_user(request):
    logout(request)
    messages.success(request, ("You have successfully logged out "))
    return redirect("index")

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("User has been Updated"))
            return redirect("update_profile")
        return render(request, 'update_user.html', {"form":form})
    else:
        messages.success(request, ("You have to login first"))
        return redirect("index")
            
            
    


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username created, Please fll out your User information"))
            return redirect('update_profile')
        else:
            for err in list(form.errors.values()):
                messages.error(request, err)
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product':product})

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})