import myfunctions as mf

while True:
  speech = mf.receive(port=9000)
  print(speech)
  mf.speak(say=speech)
