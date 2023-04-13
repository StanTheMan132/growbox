from rest_framework import serializers
from .models import Input, Output, Value, State


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input 
        read_only_fields = ("pk",)
        fields = ["pk", "name", "pin", "interval"]

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output 
        read_only_fields = ("pk",)
        fields = ["pk", "name", "type", "pin", "interval"]

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value 
        fields = ["pk", "value", "created_at", "input"]

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State 
        fields = ["pk", "value", "on_time", "off_time", "output", "created_at"]
