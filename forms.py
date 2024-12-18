from flask_wtf import FlaskForm
from wtforms import StringField, DateField, EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp


class UserForm(FlaskForm):  # FlaskForm místo Form
    name = StringField(
        "Jméno",
        validators=[
            DataRequired(message="Jméno je povinné"),
            Length(min=2, max=100, message="Jméno musí mít mezi 2 a 100 znaky"),
            Regexp(
                r"^[A-Za-zá-žÁ-Ž\s]+$",
                message="Jméno může obsahovat pouze písmena a mezery",
            ),
        ],
    )
    birth_date = DateField(
        "Datum narození",
        format="%Y-%m-%d",
        validators=[DataRequired(message="Datum narození je povinné")],
    )
    email = EmailField(
        "E-mail",
        validators=[
            DataRequired(message="E-mail je povinný"),
            Email(message="Zadejte platný e-mail"),
        ],
    )
