from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddTasksView.as_view(), name='view_all_tasks'),
]