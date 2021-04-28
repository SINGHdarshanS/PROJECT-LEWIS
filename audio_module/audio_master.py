import myfunctions as mf

speech = ""

while True:
  print("Listening")
  wav = mf.listen(text=speech)
  with open("send.wav", 'wb') as f:
    while True:
      bytes_read = client_socket.recv(BUFFER_SIZE)
      if not bytes_read:
        break
      f.write(bytes_read)
  mf.send("send.wav")
  # if receive doesn't want to say something it shoudl return "" else returns phrase to be spoken
  speech = mf.receive()
