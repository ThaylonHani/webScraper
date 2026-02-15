from flask import Flask, render_template, jsonify
from scraper import get_financial_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/financeiro")
def financeiro():
    dados = get_financial_data()
    return jsonify(dados)

app.run(debug=True)
