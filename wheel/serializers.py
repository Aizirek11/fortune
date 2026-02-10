from rest_framework import serializers
from .models import Option, SpinHistory

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class SpinHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpinHistory
        fields = ['options_snapshot', 'result', 'created_at']

