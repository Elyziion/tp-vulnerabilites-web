from flask import Flask

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)