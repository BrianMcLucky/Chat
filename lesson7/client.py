import common.utils as utils
import common.variables as variables
import logging
import select

logger = logging.getLogger('chat.client')


def main():
    logger.debug('Start...')
    user_name = input('Enter username>>>')

    parser = utils.parser()
    names = parser.parse_args()

    sock = utils.get_user_socket(names.addr, names.port)
    server_addr = sock.getpeername()
    print(f'Connected to {server_addr[0]}:{server_addr[1]}')

    variables.PRESENCE['user']['account_name'] = user_name
    try:
        utils.send_data(sock, variables.PRESENCE)
        logger.info(f'Presence send to {server_addr} : {variables.PRESENCE}')

    except ConnectionResetError as c:
        logger.error(c)
        sock.close()
        exit(1)

    while True:
        rr = []

        try:
            rr, ww, ee = select.select([sock], [], [], 1)
        except Exception as e:
            pass

        if sock in rr:
            try:
                data = utils.get_data(sock)
            except ConnectionResetError as e:
                logger.error(e)
                break

            if data['response'] != '200':
                logger.debug('End...')
                break

            if 'messages' in data:
                for message in data['messages']:
                    print(f'{message["time"]} - {message["from"]}: {message["message"]}')

        else:
            msg = input('Введите сообщение ("exit" для выхода): ')
            if msg == "exit":
                exit(0)
            if msg:
                variables.MESSAGE['message'] = msg

                try:
                    utils.send_data(sock, variables.MESSAGE)
                except ConnectionResetError as e:
                    logger.error(e)
                    break

    sock.close()


if __name__ == '__main__':
    main()
