import pywhatkit as pwt

def send_message(phone_number,value,ticker):

    text = f"""Prezado Henrique, segue o valor do último fechamento da empresa {ticker} :\nValor do Fechamento: R$ {value}"""

    pwt.sendwhatmsg_instantly(phone_number,text)
