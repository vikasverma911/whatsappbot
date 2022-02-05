from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bot.views import UserViewSet, bot

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', bot),
]
urlpatterns = urlpatterns + router.urls
