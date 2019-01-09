#!/usr/bin/env python3
#srv
#by boot1110001

### IMPORTS ####################################################################
import sys
import socket

### NON EDITABLE VARIABLES #####################################################


### EDITABLE VARIABLES #########################################################
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

### FUNCTIONS ##################################################################


### MAIN #######################################################################
def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])