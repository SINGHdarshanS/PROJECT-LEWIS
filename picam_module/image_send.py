import socket
import tqdm
import os
import time

tick = time.time()

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "192.168.8.233"
port = 8000
filename = '1sec.mp4'
filesize = os.path.getsize(filename)

s = socket.socket()
s.connect((host, port))
print('connected')

s.send('{}{}{}'.format(filename, SEPARATOR, filesize).encode())
progress = tqdm.tqdm(range(filesize), "Sending {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            progress.close()
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
tock = time.time()-tick
# print(tock)
s.close()
