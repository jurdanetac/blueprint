from django.db import models


# Source - https://stackoverflow.com/a/8016679
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampedModel):
    # short length, use description for extended notes
    task = models.CharField(max_length=30)
    # description = models.CharField(max_length=255)
    # due_on = models.DateTime()
    # completed = models.BooleanField()
