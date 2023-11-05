from django.urls import path
from . import views


app_name = "Shop"

urlpatterns = [

    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('cart/',views.cart, name="cart"),
    path('checkout/', views.cart, name="checkout"),
    #path('sliders/', views.sliders, name="sliders"),
    #path('viewstaff/', views.viewstaff, name="viewstaff"),
    path('addComment/',views.addComment, name="addComment"),
    path('contentviews/', views.contentviews, name="content")


]