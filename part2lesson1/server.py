import common.utils as utils
import common.variables as variables
import logging
import select


logger = logging.getLogger('chat.server')


def main_serv():
    waiting = 0
    clients = []
    clients_info = {}

    logger.debug('Start...')

    parser = utils.parser()
    names = parser.parse_args()

    sock = utils.get_serv_socket(names.addr, names.port)
    serv_addr = sock.getsockname()
    print(f'Server start>>> {serv_addr[0]}:{serv_addr[1]}')
    logger.info(serv_addr)

    while True:
        messages = []

        try:
            client, client_addr = sock.accept()
        except OSError as e:
            pass
        else:
            info = f'Client connected from {client_addr[0]}:{client_addr[1]}'
            print(info)
            logger.info(info)
            client_info = {'name': '', 'addr': client_addr, 'in_messages': []}
            clients.append(client)
            clients_info[client] = client_info
        finally:
            rr = []
            ww = []
            try:
                rr, ww, ee = select.select(clients, clients, [], 0)
            except Exception as e:
                pass

            for s_client in rr:
                try:
                    data_in = utils.get_data(s_client)
                except ConnectionResetError as e:
                    logger.error(e)

                if clients_info[s_client]['name'] == '':
                    if data_in['action'] == 'presence' and data_in['user']['account_name'] != '':
                        clients_info[s_client]['name'] = data_in['user']['account_name']
                        variables.RESPONSE['response'], variables.RESPONSE['alert'] = variables.SERVER_RESP[0]
                        print(f'{data_in["time"]} - {data_in["user"]["account_name"]}: {data_in["user"]["status"]}')
                    else:
                        variables.RESPONSE['response'], variables.RESPONSE['alert'] = variables.SERVER_RESP[1]

                if clients_info[s_client]['name'] != '' and data_in['action'] == 'msg':
                    data_in['from'] = clients_info[s_client]['name']
                    print(f'{data_in["time"]} - {data_in["from"]}: {data_in["message"]}')
                    variables.RESPONSE['response'], variables.RESPONSE['alert'] = variables.SERVER_RESP[0]

                    messages.append(data_in)

                    if data_in['message'] == 'exit':
                        variables.RESPONSE['response'], variables.RESPONSE['alert'] = variables.SERVER_RESP[2]

                clients_info[s_client]['data_out'] = variables.RESPONSE

            for s_client in clients:
                clients_info[s_client]['in_messages'].extend(messages)

            for s_client in ww:
                if 'data_out' in clients_info[s_client]:
                    data_out = clients_info[s_client]['data_out']
                    data_out['messages'] = clients_info[s_client]['in_messages']

                    try:
                        utils.send_data(s_client, data_out)
                        clients_info[s_client].pop('data_out')
                        clients_info[s_client]['in_messages'].clear()
                    except ConnectionResetError as e:
                        logger.error(e)
                        clients.remove(s_client)
                        clients_info.pop(s_client)

                    if data_out['response'] != '200':
                        clients.remove(s_client)
                        clients_info.pop(s_client)

        if len(clients) == 0:
            waiting += 1

        if waiting > 1500:
            break

    sock.close()
    logger.debug('End...')


if __name__ == '__main__':
    main_serv()
