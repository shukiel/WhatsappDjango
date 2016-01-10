from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
MAX_CHARS_TO_SHOW_IN_TITLE = 20


class Message (models.Model):
    message_text = models.TextField(max_length=255)
    time_created = models.DateTimeField("TimeCreated", default=now)
    message_from = models.ForeignKey (User, related_name="message_from")
    message_to = models.ForeignKey   (User, related_name="message_to")

    def __str__(self):
        res = '' + self.time_created.__str__() + ' - From ' + self.message_from.__str__()
        if len(self.message_text.__str__()) > MAX_CHARS_TO_SHOW_IN_TITLE:
            return res
        return res + ' : ' + self.message_text.__str__()