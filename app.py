from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string as st
import random as rd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# ✅ Define URL model here
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

# ✅ Function to generate unique short code
def generate_short_code():
    characters = st.ascii_letters + st.digits
    while True:
        short_code = ''.join(rd.choices(characters, k=6))
        existing_code = URL.query.filter_by(short_code=short_code).first()
        if not existing_code:
            return short_code

# ✅ Home route with GET and POST handling
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("original_url")
        
        # Generate short code and save to DB
        short_code = generate_short_code()
        new_url = URL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()
        
        # Construct full short URL
        short_url = request.host_url + "s/" + short_code
        
        return render_template("index.html", short_url=short_url)
    
    return render_template("index.html")

# ✅ Redirect route (to be implemented next)
@app.route("/s/<short_code>")
def redirect_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return redirect(url_entry.original_url)
    else:
        return "Invalid short URL."

if __name__ == "__main__":
    app.run(debug=True)
