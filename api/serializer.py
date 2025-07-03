from rest_framework import serializers
from .models import Users, Pets_Statuses, Admins, Availabilities, Donations, Pets, Petting_Dates, Adoptions

class PetStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets_Statuses
        fields = '__all__'

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'

class AvailabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabilities
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class DonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__'

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class PettingDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petting_Dates
        fields = '__all__'

class AdoptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoptions
        fields = '__all__'