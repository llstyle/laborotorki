from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import ClientSerializer, ClientCreateSerializer
from django.shortcuts import render, redirect
from rest_framework import viewsets



class UserProfileListCreateView(ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientCreateSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
       return self.queryset.get(user__username=self.kwargs.get('username'))


def register(request):
    print(request.user)
    return render(
        request,
        'blogAuth/registration.html',
    )


class ClientDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
       return self.queryset.get(user__id=self.kwargs.get('id'))


def login(request):
    return render(
        request,
        'blogAuth/login.html',
    )

