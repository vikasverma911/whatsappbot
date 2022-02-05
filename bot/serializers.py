from rest_framework import serializers
from .models import Message, User

class UserSerializer(serializers.ModelSerializer):
    message = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['ProfileName', 'WaId', 'message']
