from django.urls import path
from .views import mangaByUpdate
app_name = 'mangaByUpdate'
urlpatterns = [
    path('frontpage/', mangaByUpdate, name = 'mangaByUpdate')
]