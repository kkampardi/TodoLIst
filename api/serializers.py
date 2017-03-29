from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    # This serializer maps the model instance into JSON format

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'created', 'modified')
        read_only_fields = ('created', 'modified')
