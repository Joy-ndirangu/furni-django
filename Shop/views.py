from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "index.html",{ 'navbar': 'home'})


def shop(request):
    return render(request, "shop.html",{ 'navbar': 'shop'})


def about(request):
    return render(request, "about.html", { 'navbar': 'about'})


def services(request):
    return render(request, "services.html", { 'navbar': 'services'})

def blog(request):
    return render(request,"blog.html", { 'navbar': 'blog'})

def contact(request):
    return render(request,"contact.html", { 'navbar': 'contact'})

def cart(request):
    return  render(request, "cart.html", { 'navbar': 'cart'})

def checkout(request):
    return render(request, "checkout.html",{ 'navbar': 'checkout'})
