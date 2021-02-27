import socket
import tqdm
import os
import signal
import sys

def sig_hand(sig, frame):
    print('\nConnection aborted by user. Socket being terminated...\n')
    s.shutdown(2)
    s.close()
    sys.exit("Socket connection closed successfully. Thank you for doing business with us today here at Home Depot.")

signal.signal(signal.SIGINT, sig_hand)
SERVER_HOST = "192.168.8.233"
SERVER_PORT = 8000
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
# s.listen(5)
# print('listening')

# client_socket, address = s.accept()
# print('{} is connected'.format(address))

while True:
    s.listen(5)
    print('listening')
    client_socket, address = s.accept()
    print('{} is connected'.format(address[0]))
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), "receiving {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                progress.close()
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
