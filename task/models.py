from django.db import models


class Task(models.Model):
    """Задачи"""
    title = models.CharField("Задача", max_length=100)
    is_completed = models.BooleanField("Выполнена ли", default=False)

    def __str__(self):
        return self.title
