from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTaskListView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("tasks/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:task_id>/assign/", TaskAssignView.as_view(), name="task-assign"),
    path("users/<int:user_id>/tasks/", UserTaskListView.as_view(), name="user-tasks"),
]