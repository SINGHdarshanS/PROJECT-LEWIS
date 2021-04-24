import socket
# import tqdm
import os
# from glob import glob
import pyttsx3
import speech_recognition as sr

def send(file):
  
  SEPARATOR = "<SEPARATOR>"
  BUFFER_SIZE = 4096
  host = "192.168.8.240"
  port = 8001
  PATH = "/home/pi/PROJECT-LEWIS/"
  filename = file
  filesize = os.path.getsize(PATH+filename)
  
  s = socket.socket()
  s.connect((host, port))
  print('connected')

  s.send('{}{}{}'.format(filename, SEPARATOR, filesize).encode())
  with open(PATH+filename, "rb") as f:
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
#  os.remove(file)
  
  return 0

def speak(text=""):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()
  return 0

def listen(prompt=""):
  if(text!=""):
    speak(text=prompt)
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    return  r.listen(source, phrase_time_limit=8)
