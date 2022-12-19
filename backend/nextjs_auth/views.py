# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserSerializer,
    GroupSerializer,
    ExampleTokenObtainPairSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExampleTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = ExampleTokenObtainPairSerializer
