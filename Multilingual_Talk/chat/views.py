from django.shortcuts import render
import random
import string
from chat import models
from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def chatRoom(request):
    if('msg' in request.POST):
        models.Message.sendAMessage(request.session['chatroom'], request.session['userID'], request.POST['msg'])
    return render(request, 'chat-room.html')

def error(request):
    return render(request, 'error.html')

def leave(request):
    models.ChatRoom.leave(request.session['chatroom'], request.session['userID'])

def requestMessages(request):
    full = models.ChatRoom.checkIfFull(request.session['chatroom'])
    messages = models.Message.getAllFromChatRoom(request.session['chatroom'])
    return render(request, 'messages.html', {
        "full" : full,
        "messages" : messages,
        "userID" : request.session['userID'],
    })

def match(request):
    try:
        lang = request.POST['lang']
        native = request.POST['native']
        request.session['userID'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
        chatroom = models.ChatRoom.findAMatch(request.session['userID'], lang, native)
        request.session['chatroom'] = chatroom.room_id
        return redirect('chatRoom')
    except:
        return redirect('error')
