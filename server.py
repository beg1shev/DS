import socket
import os
import re

def filename(s):
    base_name = s[:s.index('#')]
    ind = base_name.index(".")
    name, extension = base_name[:ind], base_name[ind + 1:]

    pattern = f"{name}(_copy(\d+))?\.{extension}"
    maxi = -1
    for x in os.listdir("output"):
        q = re.search(pattern, x)
        if q is None:
            continue
        if q[2] is None:
            maxi = max(maxi, 0)
        else:
            maxi = max(maxi, int(q[2]))

    if maxi == -1:
        return base_name
    else:
        return f"{name}_copy{maxi + 1}.{extension}"


def recieve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('127.0.0.1', 8800))
    s.listen(1)

    while True:
        print("Server is started")
        connection, address = s.accept()

        print("Client connected ip:"+ str(address))

        while True:
            data = connection.recv(32)

            if data != b'':  
                data = connection.recv(32)
                file_name = filename(data.decode('utf-8'))
                output = open("/" + file_name, "wb")

                while data != b'':
                    data = connection.recv(32)
                    output.write(data)
                output.close()
                break
        
    s.close()


recieve()
