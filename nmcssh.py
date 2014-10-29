#!/usr/bin/env python
from __future__ import print_function
from argparse import ArgumentParser
from jsonrpclib import Server
import sys
import os

PREFIX = 'ssh'

def get_rpc_string(path):
    with open(path) as f:
        conf_str = f.read()

    config = {}

    for x in conf_str.split():
        key, value = x.split('=')
        config[key] = value

    return 'http://%s:%s@127.0.0.1:%s' % (config['rpcuser'], config['rpcpassword'], config['rpcport'])


def main():
    args = parser.parse_args()
    config = get_rpc_string(os.path.expanduser('~/.namecoin/namecoin.conf'))
    rpc = Server(config)

    try:
        entry = rpc.name_filter('^%s/%s$' % (PREFIX, args.key), 0)[0]
        print(entry['value'])
    except IndexError:
        print('Key not found', file=sys.stderr)


parser = ArgumentParser()
parser.add_argument('key', help='The key you want to lookup')

if __name__ == '__main__':
    main()
