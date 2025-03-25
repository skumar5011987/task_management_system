from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task

class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "mobile", "is_staff", "is_active")
    search_fields = ("username", "email", "mobile")
    ordering = ("id",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("role", "mobile",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("role", "mobile",)}),
    )

admin.site.register(User, CustomUserAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "task_type", "status", "created_at", "completed_at")
    search_fields = ("name", "task_type", "status")
    list_filter = ("task_type", "status")
    ordering = ("-created_at",)

admin.site.register(Task, TaskAdmin)