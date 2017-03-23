from django.test import TestCase

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
