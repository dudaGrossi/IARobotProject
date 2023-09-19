#definição das informações necessárias para ligação

from twilio.rest import Client 

account_sid = "AC9b12379e3c03247af873c6e91869ac2c"
auth_token = "83b0edaa66ac28ce807b887f2c9dbad8"
meu_numero = "+5537988247540"
numero_twilio = "+12565888741"

#faz a ligação com a conta twilio
client = Client(account_sid, auth_token)

mensagem = """ 
<Response>
<Say language="pt-BR">
Oi, Duda! Tá tudo bem? Estão precisando da sua ajuda.
</Say>
</Response>
"""

ligacao = client.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)