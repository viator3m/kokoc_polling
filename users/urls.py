from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('all/', views.users_list, name='all'),
    path('profile/', views.profile, name='profile'),
    path('color/', views.color, name='color'),
    path('style/', views.style, name='style'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),
]
