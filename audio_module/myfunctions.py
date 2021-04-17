# import socket
# import tqdm
# import os
# from glob import glob

def send(file):
  
  SEPARATOR = "<SEPARATOR>"
  BUFFER_SIZE = 4096
  host = "192.168.8.240"
  port = 8000
  PATH = "/home/pi/capstone/footage/"
  filename = 'test1.mp4'
  filesize = os.path.getsize(PATH+filename)
  
  s = socket.socket()
  s.connect((host, port))
  print('connected')

  s.send('{}{}{}'.format(filename, SEPARATOR, filesize).encode())
  progress = tqdm.tqdm(range(filesize), "Sending {}".format(filename), unit="B", unit_scale=True, unit_divisor=1024)
  with open(PATH+filename, "rb") as f:
      while True:
          bytes_read = f.read(BUFFER_SIZE)
          if not bytes_read:
              break
          s.sendall(bytes_read)
          progress.update(len(bytes_read))
#    # uncomment if latency+RTT+processing time exceeds one second to prevent file buildup
#        print('Got here')
#        files = glob.glob(PATH + '*.mp4')
#        for f in files:
#            os.remove(f)
#        break
  s.close()
  
  return 0


def receive():
  pass
