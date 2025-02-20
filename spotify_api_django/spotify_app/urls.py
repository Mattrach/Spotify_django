# users_app/urls.py
from django.urls import path
from .views import DeleteUserView, HomeView, CreateUserView, ListUserView, UserDetailView, DeleteUserView, MusicalPreferenceDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', ListUserView.as_view(), name='list-users'),  # Listar usuarios
    path('users/create/', CreateUserView.as_view(), name='create-user'),  # Crear usuario
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),  # Obtener usuario específico
    path('users/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete-user'),  # Eliminar usuario
    path('spotify/<int:user_id>/', MusicalPreferenceDetail.as_view(), name='spotify-preferences'),  # Preferencias musicales
]