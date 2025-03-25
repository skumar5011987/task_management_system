from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Task, TaskAssignment, User
from .serializers import TaskSerializer, UserRegistrationSerializer

# view to create task view
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# view to assign tasks to users
class TaskAssignView(APIView):

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        user_ids = request.data.get("user_ids", [])
        users = User.objects.filter(id__in=user_ids)
        for user in users:
            TaskAssignment.objects.get_or_create(task=task, user=user)
        return Response({
            "status": 1,
            "message": "Task assigned successfully"
        }, status=status.HTTP_200_OK)

# view to filter all tasks assigned to user
class UserTaskListView(generics.ListAPIView):

    def get_queryset(self, user_id):
        # filter all tasks assigned to user
        return Task.objects.filter(assigned_users__id=user_id)
    
    def get(self, request, user_id):
        qs = self.get_queryset(user_id=user_id)
        user_task_serializer = TaskSerializer(qs, many=True)
        return Response({
            "message":"ok",
            "data": user_task_serializer.data
        }, status=status.HTTP_200_OK)

# view to register new users 
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer