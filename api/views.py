from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import Users, Pets_Statuses, Admins, Availabilities, Donations, Pets, Petting_Dates, Adoptions
from .serializer import UserSerializer, PetStatusesSerializer, AdminsSerializer, AvailabilitiesSerializer, DonationsSerializer, PetsSerializer, PettingDatesSerializer, AdoptionsSerializer

# Pour le LOG IN :

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Utilisateur créé"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Pour le modèle USERS : 

@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    try: 
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Pour le modèle PET_STATUSES : 

@api_view(['GET'])
def get_pet_statuses(request):
    pet_statuses = Pets_Statuses.objects.all()
    serializer = PetStatusesSerializer(pet_statuses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_pet_statuses(request):
    serializer = PetStatusesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PATCH', 'DELETE'])
def pet_statuses_detail(request, pk):
    try: 
        pet_statuses = Pets_Statuses.objects.get(pk=pk)
    except Pets_Statuses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetStatusesSerializer(pet_statuses)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = PetStatusesSerializer(pet_statuses, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pet_statuses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Pour le modèle ADMINS : 

@api_view(['GET'])
def get_admins(request):
    admins = Admins.objects.all()
    serializer = AdminsSerializer(admins, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_admins(request):
    serializer = AdminsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def admins_detail(request, pk):
    try: 
        admins = Admins.objects.get(pk=pk)
    except Admins.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdminsSerializer(admins)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = AdminsSerializer(admins, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        admins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Pour le modèle AVAILABILITIES : 

@api_view(['GET'])
def get_availabilities(request):
    availabilities = Availabilities.objects.all()
    serializer = AvailabilitiesSerializer(availabilities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_availabilities(request):
    serializer = AvailabilitiesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def availabilities_detail(request, pk):
    try: 
        availabilities = Availabilities.objects.get(pk=pk)
    except Availabilities.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AvailabilitiesSerializer(availabilities)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = AvailabilitiesSerializer(availabilities, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        availabilities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Pour le modèle DONATIONS : 

@api_view(['GET'])
def get_donations(request):
    donations = Donations.objects.all()
    serializer = DonationsSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_donations(request):
    serializer = DonationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def donations_detail(request, pk):
    try: 
        donations = Donations.objects.get(pk=pk)
    except Donations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DonationsSerializer(donations)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = DonationsSerializer(donations, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        donations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Pour le modèle PETS : 

@api_view(['GET'])
def get_pets(request):
    pets = Pets.objects.all()
    serializer = PetsSerializer(pets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_pets(request):
    serializer = PetsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def pets_detail(request, pk):
    try: 
        pets = Pets.objects.get(pk=pk)
    except Pets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PetsSerializer(pets)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = PetsSerializer(pets, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Pour le modèle PETTING_DATES : 

@api_view(['GET'])
def get_petting_dates(request):
    petting_dates = Petting_Dates.objects.all()
    serializer = PettingDatesSerializer(petting_dates, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_petting_dates(request):
    serializer = PettingDatesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def petting_dates_detail(request, pk):
    try: 
        petting_dates = PettingDatesSerializer.objects.get(pk=pk)
    except Petting_Dates.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PettingDatesSerializer(petting_dates)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = PettingDatesSerializer(petting_dates, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        petting_dates.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Pour le modèle ADOPTIONS : 

@api_view(['GET'])
def get_adoptions(request):
    adoptions = Adoptions.objects.all()
    serializer = AdoptionsSerializer(adoptions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_adoptions(request):
    serializer = AdoptionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def adoptions_detail(request, pk):
    try: 
        adoptions = AdoptionsSerializer.objects.get(pk=pk)
    except Adoptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdoptionsSerializer(adoptions)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = AdoptionsSerializer(adoptions, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        adoptions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)