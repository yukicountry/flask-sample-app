from flask import Flask

app: Flask = Flask(__name__)

@app.route("/")
def show_verification_page() -> str:
    return "<p>ローカル開発環境起動確認ページ</p>"
