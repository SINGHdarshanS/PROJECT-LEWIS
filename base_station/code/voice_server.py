from socket import socket, AF_INET, SOCK_DGRAM
import os
import signal
import sys

s = None

def signal_handler(sig, frame):
    print('\nConnection Aborted. Socket being terminated remotely')
#    s.shutdown(2)
#    s.close()
    sys.exit('Socket connection terminated')

def receive_speech(PATH = ''):

    signal.signal(signal.SIGINT, signal_handler)

    SERVER_HOST = "192.168.8.240"
    SERVER_PORT = 8001
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    s = socket()
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print('listening')

    client_socket, address = s.accept()
    print('{} is connected'.format(address))

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)

    filesize = int(filesize)

    if os.path.exists(PATH+'speech.wav'):
        os.remove(PATH+'speech.wav')
    with open(PATH+'speech.wav', 'wb') as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
        print('transfer complete')
    return PATH+'speech.wav'

def send_message(message):
    addr = "192.168.8.x"
    s = socket(AF_INET, SOCK_DGRAM)
    print("Sending following message to {}:\n\n\t\'{}\'".format(addr, message))
    s.sendto(message, addr)
    
