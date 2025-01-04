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
    return render_template('index.html', records=records)

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

@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "Při mazání záznamu nastala chyba"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    user_to_update = User.query.get_or_404(id)
    form = UserForm(obj=user_to_update)  # Předvyplní formulář aktuálními hodnotami

    if request.method == "POST" and form.validate_on_submit():
        try:
            user_to_update.name = form.name.data
            user_to_update.birth_date = form.birth_date.data
            user_to_update.email = form.email.data

            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Při aktualizaci uživatele nastala chyba: {e}"

    return render_template("form.html", form=form, is_update=True, user_id=id)

if __name__ == "__main__":
    app.run(debug=True)
