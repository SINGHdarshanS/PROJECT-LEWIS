import socket
import tqdm
import os
from glob import glob

from picamera import PiCamera
from time import sleep

def send(filename):
  
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "192.168.8.240"
    port = 8000
    PATH = "/home/pi/capstone/footage/"
    filesize = os.path.getsize(filename)
  
    s = socket.socket()
    s.connect((host, port))
    print('connected')

    s.send('{}{}{}'.format(filename, SEPARATOR, filesize).encode())
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
#    # uncomment if latency+RTT+processing time exceeds one second to prevent file buildup
#        print('Got here')
#        files = glob.glob(PATH + '*.mp4')
#        for f in files:
#            os.remove(f)
#        break
    s.close()
    os.remove(filename)
    print("Transmission Complete")
    return 0


def cam_setup(camera):
    # camera.close()
    # camera = PiCamera()
    camera.resolution = (1920, 1080)
    camera.framerate = 15
    camera.exposure_mode = 'auto'
    camera.awb_mode = 'auto'
    # camera.close()
    return "Camera setup is complete"


def record(camera, PATH="/home/pi/capstone/footage/", filehead="test1"):
    location = PATH+filehead+'.h264'
    print("here")
    # camera = PiCamera()
    camera.start_recording(location)
    sleep(2)
    camera.stop_recording()
    return location
