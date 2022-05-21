from tabulate import tabulate
from task2 import host_range_ping


def host_range_ping_tab():
    tab_list = host_range_ping()
    print(tabulate([tab_list], headers='keys', tablefmt='pipe', stralign='center'))


host_range_ping_tab()
