from dotenv import load_dotenv
import requests, os


# Load environment variables from .env file
load_dotenv()

# # Stock price
# stock_params = {"symbol": "AAPL", "apikey": os.getenv("ALPHA_API_KEY")}
# stock_response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=stock_params)
# data = stock_response.json()
# yesterday = list(data["Time Series (Daily)"].keys())[0]
# # print(f"Yesterday's date: {yesterday}")
# # today = list(data["Time Series (Daily)"].keys())[1]
# # print(f"Today's date: {today}")
# price = float(data["Time Series (Daily)"][yesterday]["4. close"])
# print(f"AAPL closing price yesterday {yesterday}: ${price}")

# News API
import finnhub
import datetime

# Get dates
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Setup client
finnhub_client = finnhub.Client(api_key=os.environ.get("FINNHUB_API_KEY"))
# Company News
# Need to use _from instead of from to avoid conflict
latest_news = finnhub_client.company_news('AAPL', _from=yesterday, to=today)
print(f"Latest news for AAPL from {yesterday} to {today}:")

for news in latest_news[:5]:
    print(f"Title: {news['headline']}")
    print(f"Source: {news['source']}")
    print(f"Date: {news['datetime']}")
    print(f"Summary: {news['summary']}")
    print("-" * 50)

# Send message via Twilio WhatsApp
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token =  os.environ.get('TWILIO_AUTH_TOKEN')
print("Twilio account SID:", account_sid)
print("Twilio auth token:", auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    #content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e', # Your appointment is coming up on {1} at {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX350d429d32e64a552466cafecbe95f3c', # Thank you for your order. Your delivery is scheduled for {1} at {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX229f5a04fd0510ce1b071852155d3e75', # {1} is your verification code. For your security, do not share this code.
    #content_variables='{"1":"409173"}',    
    content_sid='HX38f4a38e390bfec8bfe8760c5d013619', # TSLA closing price: ${{1}}
    content_variables=f'{{"1":"{price}"}}',
    to='whatsapp:+447818912097'
)

print(message.sid)