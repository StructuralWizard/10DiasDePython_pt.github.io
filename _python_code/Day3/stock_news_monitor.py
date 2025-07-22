from dotenv import load_dotenv
import requests, os


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# # Preço da ação
# stock_params = {"symbol": "AAPL", "apikey": os.getenv("ALPHA_API_KEY")}
# stock_response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=stock_params)
# data = stock_response.json()
# yesterday = list(data["Time Series (Daily)"].keys())[0]
# # print(f"Data de ontem: {yesterday}")
# # today = list(data["Time Series (Daily)"].keys())[1]
# # print(f"Data de hoje: {today}")
# price = float(data["Time Series (Daily)"][yesterday]["4. close"])
# print(f"Preço de fechamento da AAPL ontem {yesterday}: ${price}")

# API de Notícias
import finnhub
import datetime

# Obter datas
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Configurar cliente
finnhub_client = finnhub.Client(api_key=os.environ.get("FINNHUB_API_KEY"))
# Notícias da Empresa
# Precisa usar _from em vez de from para evitar conflito
latest_news = finnhub_client.company_news('AAPL', _from=yesterday, to=today)
print(f"Últimas notícias da AAPL de {yesterday} a {today}:")

for news in latest_news[:5]:
    print(f"Título: {news['headline']}")
    print(f"Fonte: {news['source']}")
    print(f"Data: {news['datetime']}")
    print(f"Resumo: {news['summary']}")
    print("-" * 50)

# Enviar mensagem via WhatsApp do Twilio
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token =  os.environ.get('TWILIO_AUTH_TOKEN')
print("SID da conta Twilio:", account_sid)
print("Token de autenticação Twilio:", auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    #content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e', # Seu agendamento está chegando em {1} às {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX350d429d32e64a552466cafecbe95f3c', # Obrigado pelo seu pedido. Sua entrega está agendada para {1} às {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX229f5a04fd0510ce1b071852155d3e75', # {1} é o seu código de verificação. Para sua segurança, não compartilhe este código.
    #content_variables='{"1":"409173"}',    
    content_sid='HX38f4a38e390bfec8bfe8760c5d013619', # Preço de fechamento da TSLA: ${{1}}
    content_variables=f'{{"1":"{price}"}}',
    to='whatsapp:+447818912097'
)

print(message.sid)