from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    size = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class bag(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(product, blank=True)
    
     
class message(models.Model):
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
