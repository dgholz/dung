from __future__ import absolute_import
import simplejson as json

import zmq

def remote(func):
    def wrapper(self, *args, **kwargs):
        if not self.remote:
            return func(self, *args, **kwargs)
        else:
            self.do_remote(func, args, kwargs)
    return wrapper

class Dung(object):

    def __init__(self, remote=None):
        self.remote = remote
        self.port = int(13245)

    @remote
    def punchline(self):
        print "DUNNNNNNG!"

    def do_remote(self, func, args, kwargs):
        context = zmq.Context()
        socket = context.socket(zmq.PUSH)
        socket.connect("tcp://{0}:{1}".format(self.remote, self.port))
        socket.send(json.dumps(
            {
                'method': func.__name__,
                'args': args,
                'kwargs': kwargs,
            }
        ))

    def wait_for_it(self):
        context = zmq.Context()
        socket = context.socket(zmq.PULL)
        socket.bind("tcp://*:{0}".format(self.port))
        d = json.loads(socket.recv())
        getattr(self, d['method'])(*d['args'], **d['kwargs'])
