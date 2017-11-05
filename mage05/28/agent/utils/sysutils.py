#encoding: utf-8
import socket
import uuid

def get_uuid():
    return str(uuid.uuid1()).replace('-', '')

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def get_mac_address():
    mac=uuid.UUID(int=uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


if __name__ == '__main__':
    print(get_hostname())
    print(get_ip_address())
    print(get_mac_address())