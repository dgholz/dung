import argparse

class Joke(object):
    @staticmethod
    def add_parser(parser):
        parser.add_parser('joke')

    def __init__(self, dung):
        self.dung = dung

    def run(self): 
        self.dung.punchline()
