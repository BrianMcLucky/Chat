from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(addresses, time=100, req=1):
    result = {'Доступные узлы': "", 'Недоступные узлы': ""}
    for address in addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        process = Popen(f'ping {address} -w {time} -n {req}', shell=False, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            result['Доступные узлы'] = f'{str(address)}\n'
            res_str = f'{address} - Узел доступен.'
        else:
            result['Недоступные узлы'] = f'{str(address)}\n'
            res_str = f'{address} - Узел недоступен.'
        print(res_str)
    return result


if __name__ == '__main__':
    ip_adr = ['yandex.ru', 'mail.ru', '198.100.01.01', 'google.com', '2.2.2.2', 'vk.com']
    host_ping(ip_adr)
