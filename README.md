# IARobotProject
Desenvolvimento de um robô social para a disciplina de IA da UFLA

**Arquitetura do Robô:**

Sentir -> Pensar -> Agir - *Arquitetura MVC*
- Sentir: controller
- Pensar (verificação): model
- Agir: view

**Algoritmos e tecnologias utilizados:**
- Pygame;
- ElevenLabs;
- Speech Recognition;
- Speech to Text;
- Twilio;
- Threading.

**Funcionamento geral:**

O programa se inicia com o aparecimento de uma tela que mostra a imagem do robô, com seu som característico e uma mensagem de cumprimento.

Posteriormente, o usuário pode escolher qual animal deseja que seu robô social seja, mudando assim a imagem exibida na tela para a correspondente ao animal escolhido, assim como o nome do robô.

Passada essa fase inicial de configuração para criar maior proximidade entre humano e robô, o usuário poderá interagir com o robô da forma que preferir:
    
    - Pode cumprimentá-lo;
    - Pode perguntar como o robô vai;
    - Pode pedir ajuda ao robô;
    - Pode se despedir do robô.

Todas essas possibilidades geram respostas específicas do robô, sendo para as duas primeiras opções respostas em voz, continuando a conversa, para o pedido de ajuda, o acionamento da API de ligação implementada para casos de emergência, e para a despedida, o encerramento do programa.

O usuário poderá conversar com o robô o quanto quiser até que diga uma das palavras reservadas para "desligar" o robô.

*Quando o programa reiniciar, todos os passos descritos anteriormente devem ser executados novamente.*
