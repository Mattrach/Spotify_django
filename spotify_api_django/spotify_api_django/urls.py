# spotify_api_django/urls.py
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar include
from spotify_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),  # Vista de inicio
    path('api/', include('spotify_app.urls')),  # Incluir las rutas de spotify_app
]
