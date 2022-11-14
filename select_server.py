# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    # Creates listener socket
    server_socket = socket.socket()
    server_socket.bind(('', port))
    server_socket.listen()

    # Adds listener socket to a new set
    socket_set = {server_socket}

    while True:
        read, _, _ = select.select(socket_set, {}, {})
        for s in read:
            
            # Checks if it is listener socket
            if s == server_socket: 
                new_socket, _ = server_socket.accept()
                print(str(new_socket.getpeername()) + ": connected")
                socket_set.add(new_socket)

            # Regular socket, recieves data
            else:
                data = s.recv(4096) 
                if not data:
                    print(str(s.getpeername()) + ": disconnected") # Disconnects if no more data
                    socket_set.remove(s)
                else:
                    print(str(s.getpeername()) + " " + str(len(data)) + " bytes: " + str(data))
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
