import socket
import json
import argparse

DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777
CONNECTIONS = 6


def get_serv_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTIONS)
    return s


def get_user_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s


def send_data(sent, data):
    sent.send(json.dumps(data).encode('utf-8'))


def get_data(sender):
    return json.loads(sender.recv(1024).decode('utf-8'))


def parser():
    pars = argparse.ArgumentParser(description='JSON instant messaging')

    pars_group = pars.add_argument_group(title='Parameters')
    pars_group.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
    pars_group.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)

    return pars
