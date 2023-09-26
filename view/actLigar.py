#arquivo que realiza a ligação 

from twilio.rest import Client 

#função que realiza uma ligação usando o Twilio
def realizaLigacao():
    #definição das variáveis com credenciais e números necessários
    account_sid = "AC9b12379e3c03247af873c6e91869ac2c"
    auth_token = "ca75fb66ca27898ffa7758c11b819605" #modificado, pois caso contrário o twilio bloqueia por estar em repositório público no github
    meu_numero = "+5537988247540"
    numero_twilio = "+12565888741"

    #estabelece a conexão com a conta Twilio usando as credenciais
    client = Client(account_sid, auth_token)

     #define uma mensagem a ser falada durante a ligação
    mensagem = """ 
    <Response>
    <Say language="pt-BR">
    Oi, Duda! Tá tudo bem? Estão precisando da sua ajuda.
    </Say>
    </Response>
    """
    #cria uma chamada telefônica com os detalhes fornecidos
    ligacao = client.calls.create(
        to=meu_numero,
        from_=numero_twilio,
        twiml=mensagem
    )
