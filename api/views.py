from django.shortcuts import render
from rest_framework import generics

from .serializers import TodoListSerializer
from .models import TodoList

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    qyery = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def create_performance(self,serializer):
        # save the POST data when user creates a new todo list

        serializer.save()