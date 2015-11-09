from django.db import models
from django.contrib.auth.models import User


# Name      : ChatUser
# Overview  : Represents a user to chat
#             status  -> status of the user in the chat
class ChatUser(User):

    ONLINE      = 'online'
    OFFLINE      = 'offline'
    STATUS_CHOICES = (
        (ONLINE,  'online'),
        (OFFLINE, 'offline'),
    )

    # Field definition
    status   = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')

    def __unicode__(self):
        return str(self.username) + " - " + self.status
    
    
    
# Name      : Message
# Overview  : Models a message sent to the chat
#             chat_user    -> user who wrote the message
#             message      -> specific message sent by the user
#             created_at   -> datetime when the message was written    
class Message(models.Model):
    
    DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
    
    chat_user  = models.ForeignKey(ChatUser)
    message    = models.CharField(max_length = 250, default = '')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        try:
            return self.chat_user.username + " - " + self.created_at.strftime(self.DATE_FORMAT) + " - '" + self.message + "'"
        except:
            return self.chat_user.username + " - '" + self.message + "'"

    def to_json_dict(self):
        return {'user': self.chat_user.username, 'message': self.message, 'created_at': self.created_at.strftime(self.DATE_FORMAT)}

        