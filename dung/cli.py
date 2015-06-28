from __future__ import absolute_import
from pkg_resources import iter_entry_points
import sys

import argparse

import dung.command
from dung import Dung

class Cli(object):
    def __init__(self):
        self.commands = dict([(_.name ,getattr(_.load(), _.name.title())) for _ in iter_entry_points(dung.command.__name__)])

    def parse_args(self):
        parser = argparse.ArgumentParser(description='''what's brown and sounds like a bell?''')
        parser.add_argument('--remote', dest='remote', action='store', default=None)
        commands = parser.add_subparsers(title='commands', dest='command_name')
        for command_name, command in self.commands.iteritems():
            command.add_parser(commands)
        args = parser.parse_args()
        if args.command_name is None:
            parser.print_help()
            sys.exit(1)
        return args

    def run(self):
        args = self.parse_args()
        remote = args.remote
        del args.remote
        self.dung = Dung(remote=remote)
        command = args.command_name
        del args.command_name
        self.commands[command](dung=self.dung, **vars(args)).run()

def main():
    Cli().run()
