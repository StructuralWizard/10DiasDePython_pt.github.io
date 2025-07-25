import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Obtém todos os títulos dos artigos
titles = soup.select("span.titleline > a")
for title in titles:
    print(title.getText())
