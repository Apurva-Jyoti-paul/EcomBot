from rest_framework import serializers
from .models import message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model= message
        fields='__all__'
