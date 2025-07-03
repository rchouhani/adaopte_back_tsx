from rest_framework import serializers
from .models import Users, Pets_Statuses

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class PetStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets_Statuses
        fields = '__all__'