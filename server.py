"""Kredible server."""

from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "gwaggies"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    return render_template("home.html")


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)