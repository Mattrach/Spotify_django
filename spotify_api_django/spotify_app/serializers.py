from rest_framework import serializers
from .models import MusicalPreference
from django.contrib.auth.models import User

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'usuario', 'correo', 'contraseña']

    def create(self, validated_data):
        # Crear el usuario con los datos validados
        user = User.objects.create_user(
            username=validated_data['usuario'],
            email=validated_data['correo'],
            password=validated_data['contraseña']
        )
        return user

# Serializador para el modelo MusicalPreference
class MusicalPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalPreference
        fields = ['user', 'genero_favorito', 'artista_favorito', 'cancion_favorita']