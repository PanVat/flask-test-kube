from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Tento import vám umožní používat SQLAlchemy v aplikaci
db = SQLAlchemy()

class User(db.Model):  # Třída User dědí od db.Model, což umožňuje používat 'query'
    __tablename__ = 'users'  # Název tabulky v databázi

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Funkce pro inicializaci databáze (pro aplikaci Flask)
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()