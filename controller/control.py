from view import sense, act
import json
import random
import threading
import time

#definindo uma imagem padrão para a interface
#definindo uma thread para lidar com a interface
class InterfaceThread(threading.Thread):
    imagem = "robot.png"

    def __init__(self, update_func):
        super().__init__()
        self.update_func = update_func
    def run(self):
        mostrarInterface(self.update_func)

#definindo uma thread para lidar com a fala   
class FalaThread(threading.Thread):
    def __init__(self, fala_str):
        super().__init__()
        self.fala_str = fala_str
    def run(self):
        falarComUsuario(self.fala_str)

#definindo uma thread para lidar com o som
class SomThread(threading.Thread):
  def __init__(self, som_str):
      super().__init__()
      self.som_str = som_str

  def run(self):
      emitirSom(self.som_str)

#função que atualiza a imagem na interface
def atualizarImagem():
  return InterfaceThread.imagem

#funções auxiliares para o uso das threads
def falarComUsuario(str):
  act.falar(str)

def mostrarInterface(str):
  act.mostrarInterface(str)

def emitirSom(str):
  act.emitirSom(str)
#fim das funções auxiliares

#função para iniciar a thread da interface
def chamarThreadInterface(funcAtualizarImagem):
   thread_interface = InterfaceThread(funcAtualizarImagem)
   thread_interface.start()
   #thread_interface.join()

#função para iniciar a thread de fala
def chamarThreadFala(fala_str):
  thread_fala = FalaThread(fala_str)
  thread_fala.start()
  thread_fala.join()

#função para iniciar a thread de som
def chamarThreadSom(som_str):
  thread_som = SomThread(som_str)
  thread_som.start()
  thread_som.join()

#função para processar a entrada de voz e responder de acordo
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
      time.sleep(30) #tempo necessário para completar a ligação antes de pedir a próxima palavra 
    else:
      #se a palavra não for reconhecida, não faz nada
      pass

#função principal para iniciar o robô
def runRobot():
  fala_str = "Oi! Tudo bem? Eu sou o Robô Pet, seu novo animal de estimação de I.A.!Eu estou ansioso para nos tornarmos amigos. Para isso, vamos começar a minha configuração. Primeiro, qual animal você deseja que eu seja"
  som_str = "robo"
  chamarThreadInterface(atualizarImagem)
  chamarThreadSom(som_str)
  chamarThreadFala(fala_str)
  
  stt = sense.speech_to_text()
  print('STT = ', stt)
  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['animais']:
          if word == "urso":          
            InterfaceThread.imagem = "bear.png"
            som_str = "urso"
            chamarThreadSom(som_str)
          elif word == "touro":
            InterfaceThread.imagem = "bull.png"
            som_str = "touro"
            chamarThreadSom(som_str)
          elif word == "coelho":
            InterfaceThread.imagem = "bunny.png"
            som_str = "coelho"
            chamarThreadSom(som_str)         
          elif word == "gato":
            InterfaceThread.imagem = "cat.png"
            som_str = "gato"
            chamarThreadSom(som_str)
          elif word == "vaca":
            InterfaceThread.imagem = "cow.png"
            som_str = "vaca"
            chamarThreadSom(som_str)
          elif word == "cachorro":
            InterfaceThread.imagem = "dog.png"
            som_str = "cachorro"
            chamarThreadSom(som_str)
          elif word == "macaco":
            InterfaceThread.imagem = "monkey.png"
            som_str = "macaco"
            chamarThreadSom(som_str)
          elif word =="panda":
            InterfaceThread.imagem = "panda.png"
            som_str = "panda"
            chamarThreadSom(som_str)
          break
      else:
        while True:
          fala_str = "Me desculpe. Por enquanto, eu ainda não consigo ser esse animal. Tente outro, por favor."
          falarComUsuario(fala_str)
          return

  fala_str = "Perfeito! Agora escolha meu nome, por favor. Pense em um nome bem legal para mim!"
  falarComUsuario(fala_str)

  nomes = sense.speech_to_text()
  print('Nome = ', nomes)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for nome in nomes:
      if nome in dataset['nomes']:
        fala_str = "Uau! Que nome lindo! Adorei! Agora aguarde só um instante enquanto eu termino a minha configuração."
        falarComUsuario(fala_str)
        break
      else: 
        fala_str = "Obrigado! Agora aguarde só um instante enquanto eu termino a minha configuração."
        falarComUsuario(fala_str)

  fala_str = "Agora que estou configurado, podemos conversar!"
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
          continuar_conversa = True  #se uma palavra não estiver em 'desligar', definimos a variável como True - conversa deve continuar
    
    #depois do loop, verificamos a variável e chamamos conversar(word) se for True
    if continuar_conversa:
      conversar(word)