from django.db import models
from django.utils import timezone


# Source - https://stackoverflow.com/a/8016679
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TodoQuerySet(models.QuerySet):
    """Encapsulates all custom database lookups for Todos."""

    def overdue(self):
        today = timezone.now().date()
        return self.filter(due_on__lt=today, completed=False).order_by("due_on")

    def pending(self):
        return self.filter(completed=False).order_by("due_on", "created_at")

    def scheduled(self):
        today = timezone.now().date()
        return self.filter(completed=False, due_on__gt=today)

    def completed(self):
        return self.filter(completed=True).order_by("-completed_at")

    def today_pending(self):
        today = timezone.now().date()
        return self.filter(due_on=today, completed=False).order_by("created_at")

    def today_completed(self):
        today = timezone.now().date()
        return self.filter(due_on=today, completed=True).order_by("-completed_at")


class Todo(TimeStampedModel):
    # short length, use description for extended notes
    task = models.CharField(max_length=30)
    due_on = models.DateField(blank=True, null=True)

    # description = models.CharField(max_length=255)

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    # Attach the custom manager to the model
    objects = TodoQuerySet.as_manager()

    @property
    def is_overdue(self):
        today = timezone.now().date()

        if not self.completed and self.due_on < today:
            return True

        return False

    def save(self, *args, **kwargs):
        # Timestamp the completion
        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
        # Reset the timestamp to null if unchecked
        elif not self.completed:
            self.completed_at = None

        super().save(*args, **kwargs)
