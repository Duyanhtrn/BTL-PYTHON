from django.urls import path
from .views import mangaByTag
app_name = 'mangaByTag'
urlpatterns = [
    path('<int:pk>/', mangaByTag, name = 'mangaByTag'),
]
