from django.shortcuts import render
from .models import Message

def lobby(request):
    messages = Message.objects.all()[::-1][0:25][::-1]
    return render(
        request,

        'chat/index.html', context={'messages': messages}
    )
