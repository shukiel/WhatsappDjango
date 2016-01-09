from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth import views as auth_views
# Create your views here.


def index(request):
    cur_usr = request.user
    return render(request, 'messaging/index.html', {'cur_usr' : cur_usr})



@login_required
def messages(request):
    cur_usr = request.user
    return render(request, 'messaging/messages.html', {'cur_usr': cur_usr})

