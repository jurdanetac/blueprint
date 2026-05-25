from django.db import models


class Todo(models.Model):
    # short length, use description for extended notes
    task = models.CharField(max_length=30)
    # description = models.CharField(max_length=255)
    # due_on = models.DateTime()
    # completed = models.BooleanField()
