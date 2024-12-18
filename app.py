from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#TODO nainstalovat migrations a wtforms

# Kvůli erroru, který zabraňuje vytvoření databáze
with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template('index.html')

# Routa pro formulář
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        birth_date = request.form["birth_date"]
        email = request.form["email"]
        new_user = User(name=name, birth_date=birth_date, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except:
            return "Při přidávání nového uživatele nastal problém"
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
