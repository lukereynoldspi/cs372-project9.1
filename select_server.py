# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    server_socket = socket.socket()
    server_socket.bind(('', port))
    server_socket.listen()

    socket_set = {server_socket}

    while True:
        read, _, _ = select.select(socket_set, {}, {})
        for s in read:
            print(s.getpeername())
            if s == server_socket:
                new_socket = s.accept()
                socket_set.add(new_socket)
            else:
                data = s.recv(4096)
                if data == 0:
                    socket_set.remove(s)

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
