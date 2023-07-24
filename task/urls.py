from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

app_name = 'api/task'

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='project-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='project-retrieve-update-delete'),
]