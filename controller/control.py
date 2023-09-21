from view import sense, act
import json
import random
import threading

class InterfaceThread(threading.Thread):
    def __init__(self, interface_str):
        super().__init__()
        self.interface_str = interface_str

    def run(self):
        mostrarInterface(self.interface_str)

class FalaThread(threading.Thread):
    def __init__(self, fala_str):
        super().__init__()
        self.fala_str = fala_str

    def run(self):
        falarComUsuario(self.fala_str)

#funções auxiliares para o uso das threads
def falarComUsuario(str):
  act.falar(str)

def mostrarInterface(str):
  act.mostrarInterface(str)

def runRobot():

  interface_str = "robot.png"
  fala_str = "Oi! Tudo bem? Sou seu mais novo amigo robô! Para começarmos, qual animal você deseja que eu seja?"

  thread_interface = InterfaceThread(interface_str)
  thread_fala = FalaThread(fala_str)

  thread_interface.start()
  thread_fala.start()

  thread_fala.join()
  
  #coloca a imagem do robozinho, ele se apresenta e já solta "qual animal você deseja?"
  #mostrarInterface("robot.png")
  #falarComUsuario("Oi! Tudo bem? Sou seu mais novo amigo robô! Para começarmos, qual animal você deseja que eu seja?")
  stt = sense.speech_to_text()
  print('STT = ', stt)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['cumprimentos']:
        falarComUsuario(random.choice(dataset['resCumprimentos']))
        break
      elif word in dataset['despedidas']:
        falarComUsuario(random.choice(dataset['resDespedidas']))
        break
      elif word in dataset['ajuda']:
        act.ligar()
        break
      elif word in dataset['animais']:
        if word == "urso":
          mostrarInterface("bear.png")
        elif word == "touro":
          mostrarInterface("bull.png")
        elif word == "coelho":
          mostrarInterface("bunny.png")
        elif word == "gato":
          mostrarInterface("cat.png")
        elif word == "vaca":
          mostrarInterface("cow.png")
        elif word == "cachorro":
          mostrarInterface("dog.png")
        elif word == "macaco":
          mostrarInterface("monkey.png")
        elif word =="panda":
          mostrarInterface("panda.png")
        break

  thread_interface.join()