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

def chamarThreadInterface(interface_str):
   thread_interface = InterfaceThread(interface_str)
   thread_interface.start()
   thread_interface.join()

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
        fala_str = random.choice(dataset['resCumprimentos'])
        thread_fala = FalaThread(fala_str)
        thread_fala.start()
        thread_fala.join()
        break
      elif word in dataset['despedidas']:
        fala_str = random.choice(dataset['resDespedidas'])
        thread_fala = FalaThread(fala_str)
        thread_fala.start()
        thread_fala.join()
        break
      elif word in dataset['ajuda']:
        act.ligar()
        break
      elif word in dataset['animais']:
        thread_interface.join()
        if word == "urso":          
          interface_str = "bear.png"
          chamarThreadInterface(interface_str)
        elif word == "touro":
          interface_str = "bull.png"
          chamarThreadInterface(interface_str)
        elif word == "coelho":
          interface_str = "bunny.png"
          chamarThreadInterface(interface_str)          
        elif word == "gato":
          interface_str = "cat.png"
          chamarThreadInterface(interface_str)
        elif word == "vaca":
          interface_str = "cow.png"
          chamarThreadInterface(interface_str)
        elif word == "cachorro":
          interface_str = "dog.png"
          chamarThreadInterface(interface_str)
        elif word == "macaco":
          interface_str = "monkey.png"
          chamarThreadInterface(interface_str)
        elif word =="panda":
          interface_str = "panda.png"
          chamarThreadInterface(interface_str)
        break