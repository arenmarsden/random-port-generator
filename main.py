import socket
from contextlib import closing
import random

MAX_PORT_RANGE = 65535

def check_port(port):
      with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            res = sock.connect_ex(('localhost', port))
            if res == 0:
                yield port

chosen_port = random.randint(0, MAX_PORT_RANGE)

while not check_port(chosen_port):
    chosen_port = random.randint(0, MAX_PORT_RANGE)

print(chosen_port)