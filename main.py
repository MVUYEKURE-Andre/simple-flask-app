from flask import Flask, render_template
from quotes import quotes
import random

app = Flask(__name__)

@app.route("/")
def home():
    quote=random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)
# print(random.choice(quotes))