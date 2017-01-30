from __future__ import unicode_literals
import random
import string
from django.db import models

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    room_id = models.CharField(max_length=6, null=False)
    message_sender = models.CharField(max_length=6)
#   ^ True if the sender is the native speaker, False if it is the learner
    message_content = models.CharField(max_length = 255, blank=True, null=True, default="")

    @staticmethod
    def sendAMessage(room_id, sender, content):
        message = Message(room_id=room_id, message_sender=sender, message_content=content)
        message.save()
        return message

    @staticmethod
    def getAllFromChatRoom(room_id):
        return Message.objects.filter(room_id=room_id)

class ChatRoom(models.Model):
    room_id = models.CharField(max_length=6, primary_key=True, null=False)
    language = models.CharField(max_length=20, null=False)
    native = models.CharField(max_length=6, null=True)
    learner = models.CharField(max_length=6, null=True)

    @staticmethod
    def findAMatch(user, lang, native):
        # Find Available Rooms
        if(native == 'True'):
            available = ChatRoom.objects.filter(language=lang, native=None)
        else:
            available = ChatRoom.objects.filter(language=lang, learner=None)
        # If available, pick the first one, otherwise create a new room
        print(available)
        if not available:
            room_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
            match = ChatRoom(language=lang, room_id=room_id)
        else:
            match = available[0]
        # Add new user to the room
        if(native == 'True'):
            match.native = user
        else:
            match.learner = user

        match.save()
        return match

    @staticmethod
    def checkIfFull(room_id):
        available = ChatRoom.objects.filter(room_id=room_id)
        if available:
            if (available[0].native != None and available[0].learner != None):
                return True
        return False

    @staticmethod
    def checkIfLeft(room_id):
        available = ChatRoom.objects.filter(room_id=room_id)
        if available:
            if (available[0].native == 'left' and available[0].learner == 'left'):
                return True
        return False
