from common.utils import get_serv_socket, get_data, send_data, parser
from common.variables import RESPONSE, SERVER_RESP

user_name = ''

parser = parser()
names = parser.parse_args()

sock = get_serv_socket(names.addr, names.port)
serv_addr = sock.getsockname()
print(f'Server start>>> {serv_addr[0]}:{serv_addr[1]}')

user, address = sock.accept()
print(f'User connected {address[0]}:{address[1]}')

while True:
    data = get_data(user)

    if user_name == '':
        if data['action'] == 'presence' and data['user']['account_name'] != '':
            user_name = data['user']['account_name']
            RESPONSE['response'], RESPONSE['alert'] = SERVER_RESP[0]
            print(f'{data["time"]} - {data["user"]["account_name"]}: {data["user"]["status"]}')
        else:
            RESPONSE['response'], RESPONSE['alert'] = SERVER_RESP[1]

    if RESPONSE['response'] != '200':
        user.close()
        break

sock.close()
