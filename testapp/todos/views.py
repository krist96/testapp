from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from ..todos.models import Todo
from ..todos.serializers import ToDoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()