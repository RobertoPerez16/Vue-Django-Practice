from django.urls import path, include
from rest_framework import routers
from .views import ToDoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('to-do', ToDoViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]