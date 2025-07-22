from flask import Flask, render_template_string, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets

# Basic Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Needed for CSRF protection

# Define form with CSRF protection
class NameForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Route to display and handle form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.name.data}!", "success")
        return redirect('/')
    return render_template_string('''
        <!doctype html>
        <title>CSRF Example</title>
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
