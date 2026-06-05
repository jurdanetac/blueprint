from django.db import models
from django.utils import timezone


# Source - https://stackoverflow.com/a/8016679
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampedModel):
    # short length, use description for extended notes
    task = models.CharField(max_length=30)
    due_on = models.DateField(blank=True, null=True)

    # description = models.CharField(max_length=255)

    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Timestamp the completion
        if self.completed and not self.completed_on:
            self.completed_on = timezone.now()
        # Reset the timestamp to null if unchecked
        elif not self.completed:
            self.completed_on = None

        super().save(*args, **kwargs)
