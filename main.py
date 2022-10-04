from cmath import log
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


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        _name = form.inputname.data
        _email = form.inputemail.data
        _password = form.inputpassword.data
        _address = form.inputaddress.data
        _city = form.inputcity.data
        _state = form.inputstate.data
        _zips = form.inputzip.data

        user = {'name': _name, 'email': _email, 'password': _password,
                'address': _address, 'city': _city, 'zip': _zips, }
        return render_template("signupSuccess.html", user=user)

    return render_template("signup.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
