"""BackendAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api.views.status import StatusView
from api.views.signup import SignupView
from api.views.login import LoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('v1/status/', StatusView.as_view()),
    path('v1/signup/', SignupView.as_view(), name='signup_api'),
    path('v1/login/', LoginView.as_view(), name='login_api'),
    path('v1/status/', StatusView.as_view(), name='health_api'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),
]
