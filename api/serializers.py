from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Ajouter des claims personnalisés ici si besoin
        return token

    def validate(self, attrs):
        # On veut s'authentifier avec email au lieu de username
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)  # username=email car AUTH_USER_MODEL a email comme USERNAME_FIELD

        if user is None:
            raise serializers.ValidationError("Email ou mot de passe incorrect")

        data = super().validate({"username": user.username, "password": password})
        return data
