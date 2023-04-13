from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask
# Create your models here.

#output types
ON_OFF = "ON_OFF"
TIME = "TIME"

TYPE_CHOICES = (
    (ON_OFF, "on_off"),
    (TIME, "time"),
)

class Input(models.Model):
    name = models.CharField(max_length=240)
    pin = models.IntegerField()
    task = models.OneToOneField(PeriodicTask, null=True, blank=True, on_delete=models.SET_NULL)
    interval = models.IntegerField(default=60)

class Output(models.Model):
    ON_OFF = "ON_OFF"
    TIME = "TIME"

    TYPE_CHOICES = (
        (ON_OFF, "on_off"),
        (TIME, "time"),
    )

    name = models.CharField(max_length=240)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    task = models.OneToOneField(PeriodicTask, null=True, blank=True, on_delete=models.SET_NULL)
    pin = models.IntegerField()
    interval = models.IntegerField(default=60)

class Value(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    input = models.ForeignKey("Input", on_delete=models.PROTECT)

class State(models.Model):
    value = models.IntegerField()
    on_time = models.TimeField(null=True, blank=True)
    off_time = models.TimeField(null=True, blank=True)
    output = models.ForeignKey("Output", on_delete=models.PROTECT, related_name="states")
    created_at = models.DateTimeField(default=timezone.now)
