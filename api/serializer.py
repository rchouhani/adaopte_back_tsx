from rest_framework import serializers
from .models import Users, Pets_Statuses, Admins, Availabilities, Donations, Pets, Petting_Dates, Adoptions

class PetStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets_Statuses
        fields = 'status_title'

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'

class AvailabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabilities
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    availability_id = AvailabilitiesSerializer()

    class Meta:
        model = Users
        fields = '__all__'

class DonationsSerializer(serializers.ModelSerializer):
    # Je récupère les données de la table Users mises dans UserSerializer à
    # la place de user_id et je le renomme "user" plutôt que "user_id"
    user = UserSerializer(source = 'user_id')  

    class Meta:
        model = Donations
        # fields = les champs que je veux récupérer (au lieu de tout récupérer)
        fields = ['id', 'amount_euros', 'user']

class PetsSerializer(serializers.ModelSerializer):
    status = PetStatusesSerializer(source = 'status_id')
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