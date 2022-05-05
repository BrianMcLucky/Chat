import socket
import json
import argparse
import inspect
from functools import wraps
import logging

DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777
CONNECTIONS = 6


server_logger = logging.getLogger('chat.server')
client_logger = logging.getLogger('chat.client')


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        outer_func = inspect.stack()[1][3]
        server_logger.debug(f'Function "{func.__name__}" is called into "{outer_func}"')
        client_logger.debug(f'Function "{func.__name__}" is called into "{outer_func}"')
        return func(*args, **kwargs)

    return call


@log
def get_serv_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTIONS)
    return s


@log
def get_user_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s


@log
def send_data(sent, data):
    sent.send(json.dumps(data).encode('utf-8'))


@log
def get_data(sender):
    return json.loads(sender.recv(1048576).decode('utf-8'))


@log
def parser():
    pars = argparse.ArgumentParser(description='JSON instant messaging')

    pars_group = pars.add_argument_group(title='Parameters')
    pars_group.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
    pars_group.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)

    return pars
