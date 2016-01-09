from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'messaging/index.html')


def messages(request):
    return render(request, 'messaging/messages.html')