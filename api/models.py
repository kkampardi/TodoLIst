from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)