from view import sense, act
import json
import random
import threading
import queue

interface_str = ["robot.png"]

class InterfaceThread(threading.Thread):
  def __init__(self, interface_str, action_queue):
    super().__init__()
    self.interface_str = interface_str
    self.action_queue = action_queue

  def run(self):
    mostrarInterface(self.interface_str)
    self.action_queue.put("interface_done")

class FalaThread(threading.Thread):
  def __init__(self, fala_str, action_queue):
    super().__init__()
    self.fala_str = fala_str
    self.action_queue = action_queue

  def run(self):
    falarComUsuario(self.fala_str)
    self.action_queue.put("fala_done")

class SomThread(threading.Thread):
  def __init__(self, som_str, action_queue):
    super().__init__()
    self.som_str = som_str
    self.action_queue = action_queue

  def run(self):
    emitirSom(self.som_str)
    self.action_queue.put("som_done")

def falarComUsuario(str):
  act.falar(str)

def mostrarInterface(str):
  act.mostrarInterface(str)

def emitirSom(str):
  act.emitirSom(str)

def chamarThreadInterface(interface_str, action_queue):
  thread_interface = InterfaceThread(interface_str, action_queue)
  thread_interface.start()

def chamarThreadFala(fala_str, action_queue):
  thread_fala = FalaThread(fala_str, action_queue)
  thread_fala.start()

def chamarThreadSom(som_str, action_queue):
  thread_som = SomThread(som_str, action_queue)
  thread_som.start()

def runRobot():
  fala_str = "Oi! Tudo bem? Eu sou o Robô Pet, seu novo animal de estimação de I.A.!Eu estou ansioso para nos tornarmos amigos. Para isso, vamos começar a minha configuração. Primeiro, qual animal você deseja que eu seja?"
  som_str = "robo"

  action_queue = queue.Queue()
  
  chamarThreadFala(fala_str, action_queue)
  chamarThreadInterface(interface_str, action_queue)
  chamarThreadSom(som_str, action_queue)

  # Aguarda a primeira ação ser concluída antes de continuar
  for _ in range(2):
    action_queue.get()

  selecionaAcao(action_queue)

def selecionaAcao(action_queue):
  stt = sense.speech_to_text()
  print('STT = ', stt)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['animais']:
        if word == "urso":
          interface_str[0] = "bear.png"
          som_str = "urso"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "touro":
          interface_str[0] = "bull.png"
          som_str = "touro"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "coelho":
          interface_str[0] = "bunny.png"
          som_str = "coelho"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "gato":
          interface_str[0] = "cat.png"
          som_str = "gato"
          chamarThreadInterface(interface_str, action_queue)
          chamarThreadSom(som_str, action_queue)
        elif word == "vaca":
          interface_str[0] = "cow.png"
          som_str = "vaca"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "cachorro":
          interface_str[0] = "dog.png"
          som_str = "cachorro"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "macaco":
          interface_str[0] = "monkey.png"
          som_str = "macaco"
          chamarThreadInterface(interface_str, action_queue)
        elif word == "panda":
          interface_str[0] = "panda.png"
          som_str = "panda"
          chamarThreadInterface(interface_str, action_queue)
          break
      else:
        naoEhAnimal = True
        while naoEhAnimal:
          fala_str = "Me desculpe. Por enquanto, eu ainda não consigo ser esse animal. Tente outra, por favor."
          chamarThreadFala(fala_str, action_queue)

  fala_str = "Perfeito! Agora escolha meu nome, por favor. Pense em um nome bem legal para mim!"
  #chamarThreadFala(fala_str, action_queue)
  falarComUsuario(fala_str)

  nomes = sense.speech_to_text()
  print('Nome = ', nomes)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for nome in nomes:
      if nome in dataset['nomes']:
        fala_str = "Que nome lindo! Agora eu me chamo", nome
        falarComUsuario(fala_str)
        #chamarThreadFala(fala_str, action_queue)
        break

  fala_str = "Agora que estou configurado, podemos conversar!"
  falarComUsuario(fala_str)
  #chamarThreadFala(fala_str, action_queue)
  conversa = sense.speech_to_text()
  print('Conversa = ', conversa)

  for word in conversa:
    if word in dataset['cumprimentos']:
      fala_str = random.choice(dataset['resCumprimentos'])
      chamarThreadFala(fala_str, action_queue)
      break
    elif word in dataset['despedidas']:
      chamarThreadFala(fala_str, action_queue)
      break
    elif word in dataset['ajuda']:
      act.ligar()
      break
