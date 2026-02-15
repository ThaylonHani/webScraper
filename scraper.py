import requests
from bs4 import BeautifulSoup

def get_financial_data():
    url = "https://url.com.br/"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "pt-BR,pt;q=0.9",
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    json = {
        "error": 'Não encontrou a lista'
    }

    lista = soup.select_one("#lista")

    if not lista:
        return json

    itens = lista.find_all("tr")  # assumindo que são linhas
    json = []
    for item in itens:
        administradora = item.select_one('.administradora')
        values = item.select('.values')
        qtdParcelas = item.select_one('.qtdParcelas')
        valorParcelas = item.select_one('.valorParcelas')
        proximoVencimento = item.select_one('.proximoVencimento')


        json.append({
            "administradora": administradora.text.strip() if administradora else "",
            "values": [v.text.strip() for v in values] if values else [],
            "qtdParcelas": qtdParcelas.text.strip() if qtdParcelas else "",
            "valorParcelas": valorParcelas.text.strip() if valorParcelas else "",
            "proximoVencimento": proximoVencimento.text.strip() if proximoVencimento else "",
        })

    return json
