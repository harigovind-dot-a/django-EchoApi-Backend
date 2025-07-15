from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Message, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass 

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')
    list_filter = ('created_at',)