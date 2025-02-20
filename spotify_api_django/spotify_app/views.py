from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import MusicalPreference
from .serializers import MusicalPreferenceSerializer
from django.shortcuts import get_object_or_404

# Autenticación con Spotify
sp = Spotify(auth_manager=SpotifyOAuth(client_id="a3bf3c55a8b146349500da14c3628392",
                                        client_secret="852f4625b98849929a80ad31db368fac",
                                        redirect_uri="http://localhost:8888/callback",
                                        scope="user-library-read user-top-read"))


# Vista de inicio
class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Bienvenido a la API de Spotify!"})


# Crear un usuario
class CreateUserView(APIView):
    def post(self, request):
        username = request.data.get("usuario")
        password = request.data.get("contraseña")
        email = request.data.get("correo")
        
        if not username or not password or not email:
            return Response({"message": "Faltan campos requeridos: usuario, contraseña, correo"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"id": user.id, "message": f"Usuario {user.username} creado con éxito"}, status=status.HTTP_201_CREATED)


# Ver todos los usuarios
class ListUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        user_data = [{"id": user.id, "usuario": user.username, "correo": user.email} for user in users]
        return Response(user_data)


# Obtener un usuario específico
class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user_data = {
            "id": user.id,
            "usuario": user.username,
            "correo": user.email
        }
        return Response(user_data)

# Eliminar un usuario
class DeleteUserView(APIView):
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({"message": f"Usuario {user.username} eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)


# Obtener las preferencias musicales de un usuario
class MusicalPreferenceDetail(APIView):
    def get(self, request, user_id):
        try:
            preference = MusicalPreference.objects.get(user_id=user_id)
            serializer = MusicalPreferenceSerializer(preference)
            return Response(serializer.data)
        except MusicalPreference.DoesNotExist:
            return Response({"message": "Preferencias musicales no encontradas."}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request, user_id):
        data = request.data
        preference, created = MusicalPreference.objects.update_or_create(
            user_id=user_id,
            defaults={
                'genero_favorito': data.get('genero_favorito'),
                'artista_favorito': data.get('artista_favorito'),
                'cancion_favorita': data.get('cancion_favorita'),
            }
        )
        serializer = MusicalPreferenceSerializer(preference)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
