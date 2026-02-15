import requests
import re
from bs4 import BeautifulSoup


def scrape_dinamico(url, container_selector, field_selectors):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"erro": f"Erro ao acessar URL: {str(e)}"}

    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    containers = soup.select(container_selector)

    if len(containers) == 1:
        print("⚠ Atenção: Apenas 1 container encontrado. Verifique o seletor.")

    for container in containers:
        item = {}

        for field_name, selector in field_selectors.items():
            if not selector:
                continue

            match = re.match(r"(.+)\[(\d+)\]", selector)

            if match:
                base_selector = match.group(1)
                index = int(match.group(2))

                elementos = container.select(base_selector)

                if index < len(elementos):
                    item[field_name] = elementos[index].get_text(strip=True)
                else:
                    item[field_name] = None
            else:
                el = container.select_one(selector)
                item[field_name] = el.get_text(strip=True) if el else None

        if any(value is not None for value in item.values()):
            resultados.append(item)


    return resultados
