from rest_framework import serializers
from api.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('email', 'name', 'message', 'created_at')