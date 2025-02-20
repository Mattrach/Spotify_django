
from django.db import models
from django.contrib.auth.models import User

class MusicalPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo de usuario estándar
    genero_favorito = models.CharField(max_length=100, blank=True, null=True)
    artista_favorito = models.CharField(max_length=100, blank=True, null=True)
    cancion_favorita = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Preferencias musicales de {self.user.username}."
