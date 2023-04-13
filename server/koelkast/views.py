from django.db import transaction
import json
from django.shortcuts import render
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from .models import Input, Output, Value, State
from rest_framework import viewsets
from .serializers import InputSerializer, OutputSerializer, ValueSerializer, StateSerializer
from rest_framework.exceptions import APIException


# Create your views here.


class InputViewSet(viewsets.ModelViewSet):
    serializer_class = InputSerializer
    queryset = Input.objects.all()

    def preform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()

                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=instance.interval,
                    period=IntervalSchedule.SECONDS
                )

                task = PeriodicTask.objects.create(
                    interval=schedule,
                    name=f"Input: {instance.name}",
                    task="koelkast.tasks.task_monitor",
                    kwargs=json.dumps(
                        {
                            "input_id": instance.id
                        }
                    ),
                )

                instance.task = task
                instance.save()

        except Exception as e:
            raise APIException(e)

    def preform_destroy(self, instance):
        if instance.task is not None:
            instance.task.delete()
        return super().preform_destroy(instance)


    

class OutputViewSet(viewsets.ModelViewSet):
    serializer_class = OutputSerializer
    queryset = Output.objects.all()

    def preform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()

                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=instance.interval,
                    period=IntervalSchedule.SECONDS
                )

                task = PeriodicTask.objects.create(
                    interval=schedule,
                    name=f"Output: {instance.name}",
                    task="koelkasttasks.task_update",
                    kwargs=json.dumps(
                        {
                            "output_id": instance.id
                        }
                    ),
                )

                instance.task = task
                instance.save()

        except Exception as e:
            raise APIException(e)

    def preform_destroy(self, instance):
        if instance.task is not None:
            instance.task.delete()
        return super().preform_destroy(instance)

class ValueViewSet(viewsets.ModelViewSet):
    serializer_class = ValueSerializer
    queryset = Value.objects.all().order_by('-created_at')

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all().order_by('-created_at')
