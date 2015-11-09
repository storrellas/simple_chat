# Python imports
import traceback
import json

# Django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse

# Project imports
from models import ChatUser, Message

# Configure logger
import logging

log = logging.getLogger(__name__)


# Name     : test
# Overview : testing view
def test(request):
    return render(request, 'chat/room.html')


# Name     : log in
# Overview : View to log in
def chat_login(request):    
    
    try:
        # Request is to remove user
        if request.method =='POST':            
            
            log.info("LOG IN")
            username = request.POST.get('username')
            password = request.POST.get('password')
            email    = 'upwork@upwork.com'
            log.info("username -> " + username )
            log.info("password -> " + password )
            
            chat_user = ''
            try:
                chat_user = ChatUser.objects.create_user(username, email, password)
                log.info("Created user -> " + chat_user.username)
            except IntegrityError:
                chat_user =  ChatUser.objects.get(username=username)


            # Login  the user            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # redirect to Chat Room
                return redirect("/chat/room/");                            
            

    except:
        traceback.print_exc()
    
    # Render template for log in
    return render(request, 'chat/login.html')


# Name     : room
# Overview : Room for chatting
def room(request):
    
    log.info("Room for user -> " +  request.user.username)
    
    return render(request, 'chat/room.html')


# Name     : message_list
# Overview : Returns the current message list
def message_list(request):

    message_list = Message.objects.all()
    
    log.info("message_list")
    print message_list
    
    # Create array for JSON
    message_list_json = []
    for message in message_list:
        message_list_json.append(message.to_json_dict())
        
    return HttpResponse(json.dumps(message_list_json), content_type="application/json")

