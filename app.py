from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/scrap-astronaut")
def scrap_astronaut():
    try:
        url = "https://1win.com.ci/casino/play/100hp_100hpgaming_astronaut?castId=155477863141892096"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Simuler l'analyse (à améliorer selon la structure réelle)
        soup = BeautifulSoup(response.text, "html.parser")
        # Exemple fictif : récupérer une cote
        fake_cote = 2.35  # Remplacer par de vraies données scrappées

        prediction = "+2" if fake_cote > 2 else "-2"
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})￼Enter
