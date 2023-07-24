from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/project/', include('project.urls')),
    path('api/task/', include('task.urls')),
    path('api/user_management/', include('user_management.urls')),
]
