import socket
import tqdm
import os
from glob import glob
from picamera import PiCamera
from time import sleep
import myfunctions as mf
import subprocess

# camera = PiCamera()
with PiCamera() as camera:
    mf.cam_setup(camera)
    while True:
        print("recording video")
        fname = mf.record(camera)
        print("recording complete")

        # subprocess.check_output("MP4Box -add {} {}".format(fname, "to_send.mp4"), stderr=subprocess.STDOUT, shell=True)
        # print("processing done")

        #subprocess.run("MP4Box -add )
        try:
            mf.send("video.h264")
            os.remove("video.h264")
            print("file sent")
        except:
            print("No receiver detected")
            continue
