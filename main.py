from flask import Flask, render_template
from dotenv import load_dotenv
from form import SignupForm
import os


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('KEY')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/design")
def design():
    return render_template("design.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
