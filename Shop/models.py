from django.db import models

# Create your models here.

class Sliders(models.Model):
    text = models.CharField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/sliders", default="uploads/sliders/person-1.jpg")
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.name


class Product(models.Model):
        image = models.ImageField(upload_to="uploads/products", default="uploads/products/product1.jpg")
        name = models.CharField(max_length=100, blank=False, null=False)
        Price = models.CharField(max_length=100, blank=False, null=False)

        def __str__(self):
            return self.name


class Staff(models.Model):
    image = models.ImageField(upload_to="uploads/staff", default="uploads/staff.profile.jpg")
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    desc = models.CharField(max_length=500, blank=False, null=False)


    def __str__(self):
        return self.name


class Contact(models.Model):
    fname = models.CharField(max_length=100, blank=False, null=False)
    lname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False)
    message = models.TextField( blank=False)

    def __str__(self):
        return self.email
