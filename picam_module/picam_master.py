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
        fname = mf.record(camera)

        # subprocess.check_output("MP4Box -add {} {}".format(fname, "to_send.mp4"), stderr=subprocess.STDOUT, shell=True)
        print("processing done")

        mf.send(fname)
