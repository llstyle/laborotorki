from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import ClientSerializer
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from  django.contrib.auth import authenticate,login as auth_login
from rest_framework.response import Response


class UserProfileListCreateView(ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
       return self.queryset.get(user__username=self.kwargs.get('username'))


class UserAuthView(APIView):
    def post(self, request, format=None):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print(request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
       return self.queryset.get(user__username=self.kwargs.get('username'))


def login(request):
    return render(
        request,
        'blogAuth/login.html',
    )

