from rest_framework import serializers
from .models import User, Task, TaskAssignment

# User register serializer class
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "username", "email", "gender", "role", "mobile", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            gender = validated_data["gender"],
            role = validated_data.get("role"),
            mobile=validated_data.get("mobile", ""),
        )
        return user

# User serializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("id", "username", "email", "gender", "role", "mobile")

# Task serializer class
class TaskSerializer(serializers.ModelSerializer):
    # assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model=Task
        fields = ("id", "name", "description", "task_type", "status", "blocked_reason", "created_at", "completed_at",)

# task asssignement class
class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = "__all__"