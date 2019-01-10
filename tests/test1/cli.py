#!/usr/bin/env python3
#cli
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
        s.connect((HOST, PORT))
        while True:
            mystr=input('[<--] To send:  ')
            s.sendall(str.encode(mystr))
            mybytes = s.recv(1024)
            responsestr=mybytes.decode()
            print('[-->] Received: '+responsestr)

### EXEC #######################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
