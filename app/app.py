from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "🚀 Keep Hustling, Bro!",
    "🔥 Code, Eat, Sleep, Repeat!",
    "💻 Python is ❤️",
    "🎮 Gamer by night, Coder by day!",
    "✨ Apna time aayega!",
    "☕️ Coffee aur Code!"
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    html_content = f"""
    <html>
        <head>
            <title> ARPIT OP Quote Machine ⚡️</title>
            <meta http-equiv="refresh" content="1">
        </head>
        <body style="background-color:black; color:white; text-align:center; margin-top:100px;">
            <h1>{quote}</h1>
            <p style="font-size:14px; color:gray;">(Auto-refreshing every 1 second)</p>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

