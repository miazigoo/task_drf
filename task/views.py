from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import Task
from task.serializers import TaskListSerializer, TaskCreateSerializer


class TaskView(APIView):
    """
    Вывод списка задач / Добавление задачи
    для post-запроса используйте следующий пример:
    {
    "title": "Купить хлеб"
    }
    """
    def get(self, request):
        tasks = Task.objects.filter(is_completed=False)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        task = TaskCreateSerializer(data=request.data)
        if task.is_valid():
            task.save()
            data = {
                "status": "success"
            }
            return Response(status=201, data=data)
        else:
            data = {
                "error": "Поле 'title' не может быть пустым или больше 100 символов "
            }
            return Response(data=data)