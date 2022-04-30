import utils

from common.variables import PRESENCE
from log import client_log_config
import logging

logger = logging.getLogger('chat.client')


def main():
    logger.debug('Start...')
    user_name = input('Enter username>>>')

    parser = utils.parser()
    names = parser.parse_args()

    sock = utils.get_user_socket(names.addr, names.port)

    server_addr = sock.getpeername()
    print(f'Connected to {server_addr[0]}:{server_addr[1]}')

    PRESENCE['user']['account_name'] = user_name
    try:
        utils.send_data(sock, PRESENCE)
        logger.info(f'Presence send to {server_addr} : {PRESENCE}')

    except ConnectionResetError as c:
        logger.error(c)
        sock.close()
        exit(1)

    while True:
        try:
            data = utils.get_data(sock)
            logger.info(f'Data received from {server_addr} : {data}')
        except ConnectionResetError as c:
            logger.error(c)
            break

        if data['response'] != '200':
            break

    logger.debug('End...')
    sock.close()


if __name__ == '__main__':
    main()
