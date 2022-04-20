from common.utils import parser, get_user_socket, send_data, get_data
from common.variables import PRESENCE

user_name = input('Enter username>>>')

parser = parser()
names = parser.parse_args()

sock = get_user_socket(names.addr, names.port)

server_addr = sock.getpeername()
print(f'Connected to {server_addr[0]}:{server_addr[1]}')

PRESENCE['user']['account_name'] = user_name
send_data(sock, PRESENCE)

while True:
    data = get_data(sock)

    if data['response'] != '200':
        break

sock.close()
