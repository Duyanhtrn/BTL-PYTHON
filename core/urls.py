from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
app_name = 'core'
urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('searchpage/', views.searchpage, name = 'searchpage'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('mangaByLikes/', views.mangaByLikes, name = 'mangaByLikes'),
    path('likedManga/', views.likedManga, name = 'likedManga'),
    path('filterView/', views.filterView, name = 'filterView'),
]