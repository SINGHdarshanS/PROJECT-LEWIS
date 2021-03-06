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
  PATH = "/home/pi/PROJECT-LEWIS/audio_module/"
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

def receive(port=7998):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(('192.168.8.132', port))
  data, addr = s.recvfrom(1024)
  print('\nReceived:\t{}\nFrom:\t\t{}\n\n'.format(data.decode(), addr[0]))
  s.close()
  return data.decode()

def speak(say=""):
  engine = pyttsx3.init()
  engine.say(say)
  engine.runAndWait()
  print(say)
  return 0

def listen(text="empty"):
  if(text!="empty"):
    speak(say=text)
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    return  r.listen(source, phrase_time_limit=8).get_wav_data()
