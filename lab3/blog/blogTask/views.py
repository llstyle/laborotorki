from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import EmailUserSend
from django.http import HttpResponse



class EmailSendAdd(APIView):
    def get(self, request, format=None):

        if request.user.is_authenticated:
            EmailUserSend.objects.create(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EmailSendDelete(APIView):
    def get(self, request, format=None):

        if request.user.is_authenticated:
            EmailUserSend.objects.get(user=request.user).delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def monitorTask(request):
    if request.user.is_superuser:
        return render(
            request,
            'blogTask/monitor.html'
        )
    else:
        return HttpResponse("Вы не админ")

def EmailApply(request):
    if request.user.is_authenticated:
        return render(
            request,
            'blogTask/emailApply.html'
        )
    else:
        return HttpResponse("Вы не заригестрированны")



