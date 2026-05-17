from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login = StringField('login/email', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    repeat_password = PasswordField("Repeat password", validators=[DataRequired()])
    surname = PasswordField("Surname", validators=[DataRequired()])
    name = PasswordField("Name", validators=[DataRequired()])
    age = PasswordField("Age", validators=[DataRequired()])
    position = PasswordField("Position", validators=[DataRequired()])
    speciality = PasswordField("Speciality", validators=[DataRequired()])
    address = PasswordField("Address", validators=[DataRequired()])
    submit = SubmitField('Submit')
