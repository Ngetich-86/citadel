from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.URLField(max_length=200, blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        swappable = 'AUTH_USER_MODEL'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True)
    quantity_in_stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('mpesa', 'mpesa'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_date = models.DateTimeField(default=timezone.now)
    reference_number = models.CharField(max_length=50, blank=True)
    notes = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.payment_type} - {self.amount} - {self.product.name}"

    class Meta:
        ordering = ['-transaction_date']
