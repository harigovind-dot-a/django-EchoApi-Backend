from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError

class Message(models.Model):
    content = models.TextField(validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
