import multiprocessing
import common.utils as utils
import common.variables as variables
import logging


logger = logging.getLogger('chat.client')


def sent(sock):
    while True:
        msg = input('Введите сообщение ("exit" для выхода): ')
        if msg == 'exit':
            exit(0)

        if msg:
            print(msg)
            variables.MESSAGE['message'] = msg

            try:
                utils.send_data(sock, variables.MESSAGE)
            except ConnectionResetError as e:
                logger.error(e)
                break


def receive(sock):
    while True:
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


if __name__ == '__main__':
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

    p_send = multiprocessing.Process(target=sent, args=(sock,))
    p_receive = multiprocessing.Process(target=receive, args=(sock,))

    p_send.start()
    p_receive.start()

    if not p_send.is_alive() or not p_receive.is_alive():
        exit(1)

    p_send.join()
    p_receive.join()
    sock.close()
