from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import post_user

urlpatterns = [
    path('register/', post_user),
    path('token/', obtain_auth_token)
]
