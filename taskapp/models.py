from django.db import models
from django.contrib.auth.models import AbstractUser


# User model
class User(AbstractUser):
    GENDER = [
        ("male", "Male"),
        ("female", "Female")
    ]
    ROLE = [
        ("manager", "Manager"),
        ("developer", "Developer"),
        ("analyst", "Analyst"),
        ("qa", "QA")
    ]
    role = models.CharField(max_length=24, choices=ROLE, default="developer")
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")

# Task Model
class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("blocked", "Blocked"),
        ("completed", "Completed"),
        ("deleted", "Deleted"),
    ]
    TASK_TYPE = [
        ("bug", "Bug"),
        ("feature", "Feature"),
        ("task", "Task"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=16, choices=TASK_TYPE, default="feature")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    blocked_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_users = models.ManyToManyField(User, through="TaskAssignment")

# Task assignment model
class TaskAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks")
    assigned_at = models.DateTimeField(auto_now_add=True)
    

