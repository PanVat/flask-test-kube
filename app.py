from flask import Flask, render_template, request, redirect
from database import db, User, init_db
from forms import UserForm  # Import vašeho formuláře

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_database.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Potřebné pro CSRF ochranu
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializace databáze
init_db(app)

@app.route('/', methods=['GET'])
def index():
    records = User.query.all()
    return render_template('index.html', tasks=records)

@app.route("/form", methods=["GET", "POST"])
def form():
    form = UserForm()  # Vytvoříme instanci formuláře
    if form.validate_on_submit():  # Pokud je formulář validní a je odeslán
        name = form.name.data
        birth_date = form.birth_date.data
        email = form.email.data
        new_user = User(name=name, birth_date=birth_date, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except:
            return "Při přidávání nového uživatele nastal problém"
    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
