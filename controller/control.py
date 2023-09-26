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

class SomThread(threading.Thread):
  def __init__(self, som_str):
      super().__init__()
      self.som_str = som_str

  def run(self):
      emitirSom(self.som_str)


#funções auxiliares para o uso das threads
def falarComUsuario(str):
  act.falar(str)

def mostrarInterface(str):
  act.mostrarInterface(str)

def emitirSom(str):
  act.emitirSom(str)
#fim das funções auxiliares

def chamarThreadInterface(interface_str):
   thread_interface = InterfaceThread(interface_str)
   thread_interface.start()
   thread_interface.join()

def chamarThreadFala(fala_str):
  thread_fala = FalaThread(fala_str)
  thread_fala.start()
  thread_fala.join()

def chamarThreadSom(som_str):
  thread_som = SomThread(som_str)
  thread_som.start()
  thread_som.join()

def conversar(str):
  with open('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    if str in dataset['cumprimentos']:
      fala_str = random.choice(dataset['resCumprimentos'])
      falarComUsuario(fala_str)
    elif str in dataset['perguntas']:
      fala_str = random.choice(dataset['resPerguntas'])
      falarComUsuario(fala_str)
    elif str in dataset['ajuda']:
      act.ligar()
    else:
      # Se a palavra não for reconhecida, não faz nada
      pass


def runRobot():
  interface_str = "robot.png"
  fala_str = "Oi!"
  som_str = "robo"
  chamarThreadInterface(interface_str)
  chamarThreadFala(fala_str)
  chamarThreadSom(som_str)
  
  stt = sense.speech_to_text()
  print('STT = ', stt)
  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['animais']:
          if word == "urso":          
            interface_str = "bear.png"
            chamarThreadInterface(interface_str)
            som_str = "urso"
            chamarThreadSom(som_str)
          elif word == "touro":
            interface_str = "bull.png"
            chamarThreadInterface(interface_str)
            som_str = "touro"
            chamarThreadSom(som_str)
          elif word == "coelho":
            interface_str = "bunny.png"
            chamarThreadInterface(interface_str) 
            som_str = "coelho"
            chamarThreadSom(som_str)         
          elif word == "gato":
            interface_str = "cat.png"
            chamarThreadInterface(interface_str)
            som_str = "gato"
            chamarThreadSom(som_str)
          elif word == "vaca":
            interface_str = "cow.png"
            chamarThreadInterface(interface_str)
            som_str = "vaca"
            chamarThreadSom(som_str)
          elif word == "cachorro":
            interface_str = "dog.png"
            chamarThreadInterface(interface_str)
            som_str = "cachorro"
            chamarThreadSom(som_str)
          elif word == "macaco":
            interface_str = "monkey.png"
            chamarThreadInterface(interface_str)
            som_str = "macaco"
            chamarThreadSom(som_str)
          elif word =="panda":
            interface_str = "panda.png"
            chamarThreadInterface(interface_str)
            som_str = "panda"
            chamarThreadSom(som_str)
          break
      else:
        while True:
          fala_str = "Desculpe"
          #fala_str = "Me desculpe. Por enquanto, eu ainda não consigo ser esse animal. Tente outro, por favor."
          falarComUsuario(fala_str)
          return

  fala_str = "Nome"
  #fala_str = "Perfeito! Agora escolha meu nome, por favor. Pense em um nome bem legal para mim!"
  falarComUsuario(fala_str)

  nomes = sense.speech_to_text()
  print('Nome = ', nomes)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for nome in nomes:
      if nome in dataset['nomes']:
        fala_str = "Nome ok"
        #fala_str = "Uau! Que nome lindo! Adorei! Agora aguarde só um instante enquanto eu termino a minha configuração."
        falarComUsuario(fala_str)
        break
      else: 
        fala_str = "Nome não"
        #fala_str = "Obrigado! Agora aguarde só um instante enquanto eu termino a minha configuração."
        falarComUsuario(fala_str)

  fala_str = "Configurado"
  #fala_str = "Agora que estou configurado, podemos conversar!"
  falarComUsuario(fala_str)

  while True:
    fala = sense.speech_to_text()
    print('STT = ', fala)

    with open('./model/dataset.json', 'r') as file:
      dataset = json.loads(file.read())
      continuar_conversa = False  
      for word in fala:
        if word in dataset['desligar']:
          fala_str = random.choice(dataset['resDespedidas'])
          falarComUsuario(fala_str)
          fala_str = "Desligando..."
          falarComUsuario(fala_str)
          return
        else:
          continuar_conversa = True  # Se uma palavra não estiver em 'desligar', definimos a variável como True - conversa deve continuar
          #conversar(word)
    
    # Depois do loop, verificamos a variável e chamamos conversar(word) se for True
    if continuar_conversa:
      conversar(word)