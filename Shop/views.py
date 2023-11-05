from django.shortcuts import render, redirect
from .models import Sliders,Product, Staff,Contact, Blog
#to show alerts import the messages class
from django.contrib import messages


# Create your views here.

def home(request):
    data = Product.objects.all()
    blogs = Blog.objects.all()
    return render(request, "index.html",{ 'navbar': 'home','data':data, 'blogs':blogs})


def shop(request):
    data = Product.objects.all()
    return render(request, "shop.html",{ 'navbar': 'shop', 'data':data})


def about(request):
    staffs = Staff.objects.all()
    slides = Sliders.objects.all()
    return render(request, "about.html", { 'navbar': 'about', 'staffs':staffs, 'slides':slides})


def services(request):
    return render(request, "services.html", { 'navbar': 'services'})

def blog(request):
    blogs = Blog.objects.all()
    return render(request,"blog.html", { 'navbar': 'blog', 'blogs':blogs})

def contentviews(request):
    blogs = Blog.objects.all()
    return render(request, "content.html", {'navbar': 'blog', 'blogs': blogs})

def contact(request):
    return render(request,"contact.html", { 'navbar': 'contact'})

def cart(request):
    return  render(request, "cart.html", { 'navbar': 'cart'})

def checkout(request):
    return render(request, "checkout.html",{ 'navbar': 'checkout'})


#sliders
#def sliders(request):
    #slides = Sliders.objects.all()
    #return render(request,"sliders.html", {'navbar':'sliders', 'slides':slides})

#def viewstaff(request):
    #staffs = Staff.objects.all()
    #return render(request, "about.html",{'staffs': staffs})

def addComment(request):
    # verifying if form method is post

    if request.method =="POST":
        # if yes gets the user input  and stores them  in a variable ith the same exact name as the input

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # creating a variable that matches the columns in the model Students with the variable names we have above

        # after comparing save everything in query using save()method

        query = Contact(fname=fname, lname=lname, email=email, message=message)
        query.save()

        # for alerts. Message below shows if saved successfully

        messages.success(request, "Message sent successfully")

        return redirect("/contact/")

    return render(request, "contact.html")

# make sure to call this function in the form action attribute.

