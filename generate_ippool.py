#!/usr/bin/python3
# -*- coding:utf-8 -*-
from string import Template
import ipaddress
import time
Pool = Template('''
ip pool pppoe_${startNumber} bas local
 gateway ${gateway} ${netmask}
 section 0 ${ip_start} ${ip_end}
 dns-server ${dns}
#
''')


def func_decorator_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        resp = func(*args, **kwargs)
        elapsed = (time.process_time() - start_time)
        print("任务使用时间:", elapsed)
        return resp
    return wrapper


def generate_pool(ip, pool_startNum=1, dns='8.8.8.8 4.4.4.4'):
    a = ipaddress.ip_network(ip)
    startNumber = pool_startNum
    gateway = a[1]
    netmask = a.netmask
    ip_start = a[2]
    ip_end = a[-2]
    dns = dns

    pool1 = Pool.substitute(
        startNumber=startNumber,
        gateway=gateway,
        netmask=netmask,
        ip_start=ip_start,
        ip_end=ip_end,
        dns=dns)
    print(pool1)


def read_iplist(path):
    iplist = open(path)
    ip = iplist.read()
    iplist.close()
    return ip


@func_decorator_time
def main():
    filepath = './iplist.txt'
    count = 1
    step = 1
    dns = '114.114.114.114 119.29.29.29'
    iplist = read_iplist(filepath).split()
    for ip in iplist:
        generate_pool(ip, count, dns)
        count = count + step


if __name__ == '__main__':
    main()
