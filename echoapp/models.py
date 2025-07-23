from django.db import models
from django.core.validators import MinLengthValidator

class Message(models.Model):
    content = models.TextField(validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
