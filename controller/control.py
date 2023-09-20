from view import sense, act
import json
import random

def runRobot():
  #coloca a imagem do robozinho e ele se apresenta 
  stt = sense.speech_to_text()
  print('STT = ', stt)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['cumprimentos']:
        act.act(random.choice(dataset['resCumprimentos']))
        break
      elif word in dataset['despedidas']:
        act.act(random.choice(dataset['resDespedidas']))
        break
      elif word in dataset['ajuda']:
        act.ligar()
        break
      elif word in dataset['animais']:
        act.ligar()
        break
