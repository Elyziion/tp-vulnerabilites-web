import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def index():
    return """
    <!doctype html>
    <html lang="fr">
        <head>
            <meta charset="utf-8">
            <title>TP DevSecOps</title>
        </head>
        <body>
            <h1>TP de sécurité web proactive</h1>
            <p>L'application Flask fonctionne.</p>
        </body>
    </html>
    """


@app.get("/recherche")
def recherche():
    nom = request.args.get("nom", "")
    connexion = sqlite3.connect(":memory:")

    try:
        connexion.execute(
            "CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT)"
        )
        connexion.executemany(
            "INSERT INTO produits (nom) VALUES (?)",
            [("clavier",), ("souris",), ("ecran",)],
        )

        # Requete parametree : la valeur est transmise separement.
        requete = "SELECT id, nom FROM produits WHERE nom = ?"
        resultats = connexion.execute(requete, (nom,)).fetchall()

        return jsonify([
            {"id": ligne[0], "nom": ligne[1]}
            for ligne in resultats
        ])
    finally:
        connexion.close()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)