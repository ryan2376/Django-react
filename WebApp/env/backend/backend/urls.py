from django.contrib import admin
from django.urls import path
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #prebuilt views that allow us to obtain our access and refresh tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name="register"),
    path('')
]
