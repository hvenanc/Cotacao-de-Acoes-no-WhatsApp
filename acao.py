import yfinance
from message import send_message

#Petrobras
ticker = 'PETR4.SA'

dados = yfinance.Ticker(ticker)
df = dados.history()

fechamento = df.Close

ultimo_fechamento = fechamento[-1]
ultimo_fechamento = round(ultimo_fechamento,2)

send_message('+5581996593910',ultimo_fechamento,ticker)

