from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.


def index(request):
    return render(request, 'messaging/index.html', {})


@login_required
def messages(request):
    cur_usr = request.user
    return render(request, 'messaging/messages.html', {'cur_usr' : cur_usr})

