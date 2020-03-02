#-*-coding:utf8;-*-
#qpy:console

import os
import sys
import random
import socket
import select
import datetime
import threading
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.05)
__author__ = 'T.V. Raman <raman@google.com>'
__copyright__ = 'Copyright (c) 2009, Google Inc.'
__license__ = 'Apache License, Version 2.0'

import androidhelper
import time

droid = androidhelper.Android()
droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
lock = threading.RLock(); os.system('cls' if os.name == 'nt' else 'clear')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name

def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [x for x in array if x]
lock = threading.RLock(); os.system('cls' if os.name == 'nt' else 'clear')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name

def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [x for x in array if x]

def colors(value):
    patterns = {
        'R1' : '\033[31;1m', 'R2' : '\033[31;2m',
        'G1' : '\033[32;1m', 'Y1' : '\033[33;1m',
        'P1' : '\033[35;1m', 'CC' : '\033[0m'
    }

    for code in patterns:
        value = value.replace('[{}]'.format(code), patterns[code])

    return value

def log(value, status='P & P :' , color='[P1]'):
    value = colors('{color}''[P1]''[{time}] [G1]{color}{status} [R1]{color}{value}[Y1]'.format(
        time=datetime.datetime.now().strftime('%H''[R1]:''[P1]%M]' '[G1][Jaka [R1]Benang'),
        value=value,
        color=color,
        status=status
    ))
    with lock: print(value)

def log_replace(value, status='WARNING', color='[P1]'):
    value = colors('{}{} ({})        [CC]\r'.format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()

class inject(object):
    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()

        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[G1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = open(real_path('/config.ini')).readlines()
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log('Frontend Domains not found. Please check config.ini', color='[Y1]')
                return
            self.log('{} Port {}'.format(self.inject_host, self.inject_port))
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(65535)
                domain_fronting(socket_client, frontend_domains).start()
        except Exception as exception:
            self.log('{} Port {}'.format(self.inject_host, self.inject_port), color='[P1]')

class domain_fronting(threading.Thread):
    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()

        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 65535
        self.daemon = True

    def log(self, value, status='*', color='[P1]'):
        log(value, status=status, color=color)
        
    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors: break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data: break
                        # SENT -> RECEIVED
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except: break
            if timeout == 10: break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '443'
            self.log('[R1]B I S [G1]M I L L A H '.format(self.proxy_host, self.proxy_port))
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            self.log('[G1]AL[R1]HAM[Y1]DUL[G1]ILL[Y1]AH  [P1]==> [G1]YA ALLAH','[R1]'.format(self.proxy_host, self.proxy_port), color='[G1]')
        except OSError:
            self.log('Connection Error', color='[G1]')
        except TimeoutError:
            self.log('{} Not Responding'.format(self.proxy_host), color='[R1]')


R = '\033[1;33m'
G = '\033[1;33m'
Y = '\033[31;1m'
C = '\033[32;1m'
P = '\033[1;33m'
R = '\033[31;1m'
G = '\033[32;1m'
Y = '\033[1;33m'


print R + 'Nama       : MUHAMMAD AMIN\n'
print G + 'Script     : TELKOMSEL OPOK 2020\n'
print Y + 'Limit      : 600 MB \n'
print C + 'Facebook   : JAKA BENANG \n'
print P + 'Whatsapp   : 0822-6619-1505\n'
print R + 'Telegram   : 0822-6619-1505 \n'
print G + 'INGAT      : JANGAN NONTON FILM BOKEP/PORN \n'
print Y + 'By         : Gretongers NTB\n'



print(colors('\n'.join([
	
            '         '
        '[G1]JANGAN LUPA BACA','[CC]' '         -----------------','[CC]'
            '         '
       
       '[P1]بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم ','[P1]' '          ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡','[CC]'
        
        
 ])))
def main():
    C = 'Masukan Password> [m] !'
    m = 'm'
    user_input = raw_input(' Masukan Password> [m]  : ')
    if user_input != m:
        sys.exit(' HURUF KECIL SEMUA PASS NYA\n')
    
    inject('127.0.0.1', '8080').start()

if __name__ == '__main__':
    main()