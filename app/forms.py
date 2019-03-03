from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from wtforms.widgets import PasswordInput
# Este archivo contiene todos los formularios del sistema.

class LoginForm(FlaskForm):
    # validators argument es para validaciones.
    # DataRequired chequea que no estén vacíos, aunque existen más validaciones.
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")

class RegisterForm(FlaskForm):
    email = EmailField('Email')
    nombre = StringField('Nombre y apellido')
    password = PasswordField('Contraseña')
    # foto?
    tipo = StringField('Tipo')
    # TURISTA
    edad = StringField('Edad')
    pais = StringField('País de origen')
    # EMPRESA
    nombreEmpresa = StringField('Nombre de la empresa')
    submit = SubmitField("Crear usuario")

class ModifyForm(FlaskForm):
    nombre = StringField('Nombre y apellido')
    password = PasswordField('Contraseña', widget=PasswordInput(hide_value=False))
    # foto?
    # TURISTA
    edad = StringField('Edad')
    pais = StringField('País de origen')
    # EMPRESA
    nombreEmpresa = StringField('Nombre de la empresa')
    submit = SubmitField("Guardar cambios")