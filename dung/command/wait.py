import argparse

class Wait(object):
    @staticmethod
    def add_parser(parser):
        parser.add_parser('wait')

    def __init__(self, dung):
        self.dung = dung

    def run(self): 
        self.dung.wait_for_it()
