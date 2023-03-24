from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Task
from .serializers import TasksSerializer

class AddTasksView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TasksSerializer(tasks, many=True)

        return Response(serializer.data)

