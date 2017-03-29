from django.test import TestCase
# test views imports
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import  TodoList

# Create your tests here.
class ModelTestCase(TestCase):
    # lets define a test suit for the todolist model


    def setUp(self):
        # define the test client and other test
        self.todolist_name = "Goto the supermarket"
        self.todolist = TodoList(name="todolist_name")


    def test_model_can_create_a_list(self):
        objects_count = TodoList.objects.count()
        self.todolist.save()
        objects_new_count = TodoList.objects.count()
        self.assertNotEqual(objects_count, objects_new_count)

# define the ViewTestCase right after the ModelTestCase


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todolist_data = {'name': 'Go to the supermarket'}
        self.response = self.client.post(
            reverse('create'),
            self.todolist_data,
            format="json"
        )

    def test_api_can_create_a_todo_list(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)