import requests
from bs4 import BeautifulSoup

def get_financial_data():
    url = "https://www.infomoney.com.br/cotacoes/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    moedas = []

    itens = soup.find_all(".[&>*:first-child]:pl-0 [&>*:last-child]:pr-0")

    for item in itens:
        moedas.append(item)

    return moedas
