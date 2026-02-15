from flask import Flask, render_template, jsonify, request
from scraper import get_financial_data
from dinamicScraper import scrape_dinamico

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/financeiro")
def financeiro():
    dados = get_financial_data()
    return jsonify(dados)


@app.route("/api/scrape")
def api_scrape():
    url = request.args.get("url")
    container = request.args.get("container")

    if not url or not container:
        return jsonify({"error": "url e container são obrigatórios"}), 400

    field_selectors = {
        "administradora": request.args.get("administradora"),
        "valor_credito": request.args.get("valor_credito"),
        "entrada": request.args.get("entrada"),
        "parcelas": request.args.get("parcelas"),
        "valor_parcelas": request.args.get("valor_parcelas"),
        "proximo_vencimento": request.args.get("proximo_vencimento")
    }

    # Remove campos vazios
    field_selectors = {k: v for k, v in field_selectors.items() if v}

    dados = scrape_dinamico(
        url=url,
        container_selector=container,
        field_selectors=field_selectors
    )

    return jsonify(dados)

app.run(debug=True)
