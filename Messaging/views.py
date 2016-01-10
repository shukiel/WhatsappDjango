from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Message
from django.utils.timezone import now



def index(request):
    cur_usr = request.user
    all_usr = User.objects.all()
    return render(request, 'messaging/index.html', {'cur_usr' : cur_usr, 'all_usr': all_usr})

@login_required
def messages(request, user_id):
    cur_usr = request.user
    to_usr  = User.objects.get(id = user_id)
    try:
        new_msg = request.POST["message"]
        if (new_msg):
            temp = Message()
            temp.time_created = now()
            temp.message_text = new_msg
            temp.message_from = cur_usr
            temp.message_to = to_usr
            temp.save()
    except (KeyError,):
        pass
    all_msg = Message.objects.order_by('time_created').filter(
    Q(message_from=to_usr) & Q(message_to=cur_usr) | Q(message_to=to_usr) & Q(message_from=cur_usr))
    return render(request, 'messaging/messages.html', {'cur_usr': cur_usr, 'to_usr':to_usr, 'all_msg' : all_msg })


def register(request):
    cur_usr = request.user
    return render(request, 'registration/register.html', {'cur_usr': cur_usr})


def newusr(request):
    username = request.POST["username"]
    password =request.POST["password"]
    repassword = request.POST["repassword"]
    if password != repassword:
        error = 'Password don\'t match!'
        return render(request, 'registration/register.html', {'error' : error, 'reusername': username})
    try:
            newuser = User.objects.create_user(username, password= password)
            newuser.save()
            login(request, authenticate(username=username, password = password))

    except(IntegrityError):
        error = "Username already exsist!"
        return render(request, 'registration/register.html', {'error':error, 'reusername': username})
    return redirect('/whatsapp')

