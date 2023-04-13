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
    else:
        return redirect('/advocates')
    
@app.route('/advocates')
def advocates_page():

    if 'email' not in session:
        return redirect('/login')
    
    relationships = crud.get_relationships_by_email(session['email'])
    advocate_list = []

    for relationship in relationships:
        advocate_list.append(relationship.advocate)


    return render_template("advocates.html", advocate_list = advocate_list)

@app.route('/calendar')
def calendar_page():

    if 'email' not in session:
        return redirect('/login')


    return render_template("calendar.html")

@app.route('/dashboard')
def dashboard():

    if 'email' not in session:
        return redirect('/login')


    return render_template("dashboard.html")

@app.route('/notifications')
def notifications():

    if 'email' not in session:
        return redirect('/login')


    return render_template("notifications.html")

@app.route('/settings')
def settings():

    if 'email' not in session:
        return redirect('/login')

    return render_template("settings.html")

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

@app.route('/logout',)
def logout():
    del session['email']
    return redirect('/')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)