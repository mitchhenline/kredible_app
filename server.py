"""Kredible server."""

from flask import Flask, render_template, request, session, redirect, flash
from jinja2 import StrictUndefined
from model import connect_to_db, db
from forms import LoginForm
import crud


app = Flask(__name__)
app.secret_key = "gwaggies"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    if 'email' not in session:
        return redirect('/login')


    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    form = LoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data


        user = crud.get_user_by_email(email)
        if not user or user.password != password:
            flash("Invalid email or password")
            return redirect("/login")
        
        session['email'] = user.id
        return redirect("/")
    
    return render_template("login.html", form = form)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)