from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return company"""
        
        return self.name

class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=70, verbose_name='first name')
    last_name = models.CharField(max_length=70, verbose_name='last name')
    email = models.EmailField(max_length=50, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username', 'first_name', 'last_name']

    def __str__(self):
        """Return user"""
    
        return f"{self.first_name} {self.last_name}"