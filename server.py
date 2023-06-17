"""Kredible server."""

from flask import Flask, render_template, request, session, redirect, flash, abort
from flask_wtf import FlaskForm
from jinja2 import StrictUndefined
from model import connect_to_db, UserAdv
from forms import LoginForm, RequestMeetingForm

import crud

app = Flask(__name__)
app.secret_key = "gwaggies"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    if 'id' not in session:
        return redirect('/login')
    else:
        return redirect('/advocates')
    
@app.route('/advocates', methods=['GET', 'POST'])
def advocates_page():


    if 'id' not in session:
        return redirect('/login')
    
    relationships = crud.get_relationships_by_id(session['id'])
    advocate_list = []


    #NOT SURE IF WE NEED THIS, check later when add the js form
    # form = RequestMeetingForm(request.form)

    # if form.validate_on_submit():  
    #     prospect_email = form.prospect_email.data
    #     print(prospect_email)
    # else:
    #     print("Form not validated")
    # add form = form to line 46 if is needed

    for relationship in relationships:
        advocate_list.append(relationship.advocate)

    return render_template("advocates.html", advocate_list = advocate_list)

@app.route('/advocates/<adv_id>', methods =['GET','POST'])
def get_advocate_info(adv_id):

    if 'id' not in session:
        return redirect('/login')

    if not UserAdv.query.filter_by(adv_id=adv_id, id = session['id']).first():
        abort(403)

    advocate = crud.get_advocate_by_id(adv_id)
    form = RequestMeetingForm(request.form)

    if form.validate_on_submit():
        prospect_email = form.prospect_email.data
        notes = form.notes.data
        print(notes)
        flash(f"Your message {notes} was sent to {prospect_email}")

    
    else:
        print('not validated')

    return render_template("view_ind_adv.html", advocate=advocate, form=form)

@app.route('/calendar')
def calendar_page():

    if 'id' not in session:
        return redirect('/login')

    return render_template("calendar.html")

@app.route('/dashboard')
def dashboard():

    if 'id' not in session:
        return redirect('/login')

    return render_template("dashboard.html")

@app.route('/notifications')
def notifications():

    if 'id' not in session:
        return redirect('/login')

    return render_template("notifications.html")

@app.route('/settings')
def settings():

    if 'id' not in session:
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
        session['id'] = user.id
        return redirect("/")
    
    return render_template("login.html", form = form)
    
@app.route('/logout')
def logout():
    del session['id']
    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)