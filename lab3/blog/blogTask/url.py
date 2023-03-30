from django.urls import path
from . import views

urlpatterns = [
    path('monitor-task/', views.monitorTask),
    path('emailSend/', views.EmailApply),
    path('email/add/', views.EmailSendAdd.as_view()),
    path('email/delete/', views.EmailSendDelete.as_view()),
]
