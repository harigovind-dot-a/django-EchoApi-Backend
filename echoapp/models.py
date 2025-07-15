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

    def clean(self):
        super().clean()
        if len(self.username) < 5:
            raise ValidationError("Username should be atleast 5 chars long.")
        elif self._raw_password is not None and len(self._raw_password) < 5:
            raise ValidationError("Password should be atleast 5 chars long.")
        else:
            pass
        EmailValidator()(self.email)

    def set_password(self, raw_password):
        self._raw_password = raw_password
        super().set_password(raw_password)