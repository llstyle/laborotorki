from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView, ClientDetailView, UserAuthView
from . import  views

urlpatterns = [
    path('register/', views.register, name='reg'),
    path('login/', views.login, name='login'),
    #gets all user profiles and create a new profile
    path("api/accounts/auth", UserAuthView.as_view()),
    path("api/accounts/all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("api/accounts/profile/view/<username>",ClientDetailView.as_view({'get': 'retrieve'}),name="profile"),
    path("api/accounts/profile/<username>",userProfileDetailView.as_view(),name="profile"),
]