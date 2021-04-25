from socket import socket
from tqdm import tqdm
import os
import signal
import sys
import subprocess
from time import sleep

def signal_handler(sig, frame):
    print('Connection Aborted. Socket being terminated remotely')
    s.shutdown(2)
    s.close()
    sys.exit('Socket connection terminated')
def receive_video(PATH=""):
    # PATH = "/home/darshy/PROJECT-LEWIS/base_station/footage/"

    signal.signal(signal.SIGINT, signal_handler)
    SERVER_HOST = "192.168.8.240"
    SERVER_PORT = 8000
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    s = socket()
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print('listening')

    client_socket, address = s.accept()
    print('{} is connected'.format(address))

# while True:
    received = client_socket.recv(BUFFER_SIZE).decode()
    print(received.split(SEPARATOR))
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename) # look up what basename() does. I believe it decodes something but I'm not sure

# does this possibly take just the filename from a path instead of the whole path? I think this is it

    filesize = int(filesize)

#    progress = tqdm(range(filesize), "receiving {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
    if os.path.exists(PATH+'1sec.h264'):
        os.remove(PATH+'1sec.h264')
        if os.path.exists(PATH+'process.mp4'):
            os.remove(PATH+'process.mp4')
    with open(PATH + '1sec.h264', "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
#                print('got here')
                break
            f.write(bytes_read)
        print('transfer complete')
    subprocess.check_output("MP4Box -add {} {}".format(PATH+"1sec.h264", PATH+"process.mp4"), stderr=subprocess.STDOUT, shell=True)
    print("processing complete")
    return PATH+'process.mp4'
