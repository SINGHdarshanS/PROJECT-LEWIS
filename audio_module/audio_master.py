import myfunctions as mf

speech = "empty"

while True:
  print("Listening")
  wav = mf.listen(text=speech)
  with open("send.wav", 'wb') as f:
    f.write(wav)
  mf.send("send.wav")
  # if receive doesn't want to say something it shoudl return "" else returns phrase to be spoken
  print("I got here mf")
  speech = mf.receive()
