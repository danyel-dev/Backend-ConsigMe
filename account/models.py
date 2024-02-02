from django.contrib.auth.models import User
from django.db import models
from datetime import datetime



class lojista(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  proprietario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  email = models.EmailField()
  phone_number = models.CharField(max_length=16)
  image = models.ImageField(blank=True, null=True, upload_to=f'lojistasImages/{datetime.now().strftime("%d_%m_%Y")}')
  cnpj = models.CharField(max_length=14)
  cep = models.CharField(max_length=8)
  state = models.CharField(max_length=20)
  city = models.CharField(max_length=50)
  district = models.CharField(max_length=50)
  street = models.CharField(max_length=50)  
  number = models.IntegerField()
  complement = models.CharField(max_length=100, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class profile(models.Model):
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
    return f'{self.user.first_name} {self.user.last_name}'


class reviews(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  profile = models.ForeignKey(profile, on_delete=models.CASCADE)
  note = models.IntegerField()
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.profile}'
