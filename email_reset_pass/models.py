from django.db import models

# Create your models here.

class SignupForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone_no = models.ImageField(max_length=10)

    def __str__(self):
        return self.username