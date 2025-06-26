from django.db import models

# Create your models here.
class Message(models.Model): # This is a model for storing messages
    content = models.TextField() # The content of the message
    created_at = models.DateTimeField(auto_now_add=True) # The timestamp when the message was created
    
    def __str__(self):
        return self.content # This method returns the string representation of the message, which is its content
