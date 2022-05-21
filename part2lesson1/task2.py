from ipaddress import ip_address
from task1 import host_ping


def host_range_ping():
    ip_adr = input('Enter first ip address>>>')
    num_ip = input('Enter  number of addresses to check>>>')

    ip_list = []
    [ip_list.append(str(ip_address(ip_adr) + i)) for i in range(int(num_ip))]
    return host_ping(ip_list)


if __name__ == '__main__':
    host_range_ping()
