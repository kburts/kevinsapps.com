from channels.routing import route, route_class
from songs.consumers import ws_connect, ws_disconnect, LogConsumer, MusicConsumer

channel_routing = [
    # route('websocket.connect', ws_connect),
    # route('websocket.disconnect', ws_disconnect),
    #route_class(MusicConsumer, path=r'/music/')
    MusicConsumer.as_route(path=r'/music/$'),
    LogConsumer.as_route(path=r'/log/$'),
]