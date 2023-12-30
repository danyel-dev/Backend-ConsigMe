from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.PROTECT)
  store_name = models.CharField(max_length=50)
  professional_email = models.EmailField()
  phone_number = models.CharField(max_length=16)
  cpf = models.CharField(max_length=11)
  birth_date = models.DateField(blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to=f'profileImages/{datetime.now().strftime("%d_%m_%Y")}')
  cep = models.CharField(max_length=8)
  state = models.CharField(max_length=20)
  city = models.CharField(max_length=50)
  district = models.CharField(max_length=50)
  street = models.CharField(max_length=50)  
  house_number = models.IntegerField()
  complement = models.CharField(max_length=100)
  quantity_products_sold = models.IntegerField(default=0, null=True, blank=True)  
  is_reseller = models.BooleanField(default=False, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
      return self.store_name
