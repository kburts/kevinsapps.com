import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.generic.websockets import JsonWebsocketConsumer, WebsocketConsumer


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)


class LogConsumer(JsonWebsocketConsumer):
    http_user = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connection_groups(self, **kwargs):
        return ['all', 'music']

    def connect(self, message, **kwargs):
        self.group_send('all', 'hello {}'.format(message.user))

    def receive(self, content, **kwargs):
        self.group_send('all', content)

    def disconnect(self, message, **kwargs):
        self.group_send('all', 'bye {}'.format(message.user))


class MusicConsumer(JsonWebsocketConsumer):

    def connection_groups(self, **kwargs):
        return ['music']

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, content, **kwargs):
        pass

    def disconnect(self, message, **kwargs):
        pass