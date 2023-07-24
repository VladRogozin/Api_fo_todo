from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDeleteView

app_name = 'api/project'

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDeleteView.as_view(), name='project-retrieve-update-delete'),
]