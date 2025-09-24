from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Pets_Statuses, Admins, Availabilities, Donations, Pets, Petting_Dates, Adoptions, User
from .serializer import UserSerializer, PetStatusesSerializer, AdminsSerializer, AvailabilitiesSerializer, DonationsSerializer, PetsSerializer, PettingDatesSerializer, AdoptionsSerializer
# for Log In
from rest_framework.views import APIView
# for Tokens
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.decorators import login_required

from rest_framework import serializers
import jwt
import datetime
from django.conf import settings

from login_required import login_not_required

User = get_user_model()

class RegisterView(APIView):
    
    def post(self, request):
        print("🔍 Payload reçu :", request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        
        # name = f"{firstname} {lastname}".strip()

        if not email or not password:
            return Response({"error": "Email et mot de passe requis."}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Cet email est déjà utilisé."}, status=400)

        user = User.objects.create_user(email=email, password=password, name=name)
        return Response({"message": "Utilisateur créé avec succès."}, status=status.HTTP_201_CREATED)



@login_not_required
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is None:
            raise serializers.ValidationError("Email ou mot de passe incorrect")
        else:
            login(request, user)
        
        # Générer un token JWT
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        print('🥦', token)
        response = Response({"message": "Connexion réussie"})
        response.set_cookie(
            key="jwt",
            value=token,
            httponly=True,
            samesite="Lax",  # 'Strict' si tu veux bloquer les requêtes cross-site
            secure=False,     # True en prod HTTPS, False en dev local HTTP
            max_age=24*3600,  # expiration 24h
        )
            
        
        return response


class LogoutView(APIView):
    def logout(self, request):
        logout(request)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
# pour l'autenthification : 

# class ProtectedView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": f"Bonjour {request.user.firstname}"})


# Pour le modèle USERS : 

@api_view(['GET'])
def get_users(request):
    print('🎲🎲🎲', request.user.is_authenticated)
    if request.user.is_authenticated:
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else: return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    try: 
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
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

@api_view(['GET'])
def get_pets_available(request):
    pets = Pets.objects.filter(status_id=1)
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