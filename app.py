from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/scrap-astronaut")
def scrap_astronaut():
    try:
        url = "https://1win.com.ci/casino/play/100hp_100hpgaming_astronaut"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Analyse simulée (à personnaliser)
        soup = BeautifulSoup(response.text, "html.parser")
        fake_cote = 2.35  # À remplacer par une valeur scrappée réelle

        prediction = "+2" if fake_cote > 2 else "-2"
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

# LIGNE IMPORTANTE POUR RENDER :
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)￼Enter
