from django.urls import path
from . import views

urlpatterns = [
    path('shots/', views.shot_list_create, name='shot-list'),
    path('shots/<int:pk>/', views.shot_detail, name='shot-detail'),
    path('practice/', views.practice_list_create, name='practice-list'),
    path('practice/<int:pk>/', views.practice_detail, name='practice-detail'),
    path('login/', views.login_view, name='login'),
    path('userprofile/', views.user_profile_view, name='user-profile'),  
]