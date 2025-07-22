from flask import Flask, render_template_string, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets

# Aplicativo Flask básico
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Necessário para proteção CSRF

# Define o formulário com proteção CSRF
class NameForm(FlaskForm):
    name = StringField('Seu Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Rota para exibir e manipular o formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Olá, {form.name.data}!", "success")
        return redirect('/')
    return render_template_string('''
        <!doctype html>
        <title>Exemplo de CSRF</title>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% for category, message in messages %}
            <div style="color:green">{{ message }}</div>
          {% endfor %}
        {% endwith %}
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name(size=20) }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
