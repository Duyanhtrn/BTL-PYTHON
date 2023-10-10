from django.urls import path
from . import views
app_name = 'manga'
urlpatterns = [
    path('<int:pk>/', views.detail, name = 'detail'),
    path('like/<int:pk>', views.LikeView, name = 'like_manga'),
]