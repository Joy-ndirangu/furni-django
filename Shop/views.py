from django.shortcuts import render, redirect
from .models import Sliders,Product, Staff,Contact
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "index.html",{ 'navbar': 'home'})


def shop(request):
    data = Product.objects.all()
    return render(request, "shop.html",{ 'navbar': 'shop', 'data':data})


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


#sliders
def sliders(request):
    slides = Sliders.objects.all()
    return render(request,"sliders.html", {'navbar':'sliders', 'slides':slides})

def viewstaff(request):
    staffs = Staff.objects.all()
    return render(request, "about.html",{'staffs': staffs})

def addComment(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')


        query = Contact(fname=fname, lname=lname, email=email, message=message)
        query.save()

        messages.success(request, "Message sent successfully")

        return redirect("/contact/")

    return render(request, "contact.html")
