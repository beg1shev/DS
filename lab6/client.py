import sys
import socket
import os
from math import ceil
from tqdm import tqdm


def convert_to_fix_len(s):
    return str.encode(s + '#' * (32 - len(s)))

def send(filename, ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    with open(filename, 'rb') as f:
        s.send(convert_to_fix_len('Start sending')
)
        s.send(convert_to_fix_len(filename))

        file_size = os.path.getsize(filename)
        bytes = 0
        for i in tqdm(range(ceil(file_size / 32))):
            data = f.read(32)
            s.send(data)
            if not data:
                print('100%')
                break

            bytes += 32
    print(bytes)
    f.close()


filename, ip, port = sys.argv[1:]
port = int(port)

send(filename, ip, port)
