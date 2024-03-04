from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('login/', views.login_page, name='user_login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_page, name='register'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change')
]