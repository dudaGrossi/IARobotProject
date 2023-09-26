import speech_recognition as sr

def speech_to_text():
  #inicializa o recognizer
  recognizer = sr.Recognizer()

  #captura o aúdio do microfone
  with sr.Microphone() as source:
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  #ajusta os ruídos
    audio = recognizer.listen(source)

  try:
    #reconhece a fala usando a Google Web Speech API
    text = recognizer.recognize_google(audio, language='pt-BR')
    text = text.lower()
    stt = text.split(' ')
    return stt
  except sr.UnknownValueError:
    print("Desculpe, eu não entendi. Você pode repetir?.")
  except sr.RequestError as e:
    print("Desculpe, algum erro ocorreu; {0}".format(e))
