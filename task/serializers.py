from rest_framework import serializers

from task.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    """Добавление задачи со значением is_completed=False"""

    class Meta:
        model = Task
        fields = ('title',)


class TaskListSerializer(serializers.ModelSerializer):
    """Вывод всех задач со значением is_completed=False"""

    class Meta:
        model = Task
        fields = "__all__"