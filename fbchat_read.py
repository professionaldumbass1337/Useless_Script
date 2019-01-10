import time
from fbchat import log, Client
from fbchat.models import *

# Subclass fbchat.Client and override required methods
class ReadBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        reply = '✔ seen ' + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min)

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(Message(text = reply), thread_id=thread_id, thread_type=thread_type)

client = ReadBot("feedism", "khongnoigrr")
client.listen()