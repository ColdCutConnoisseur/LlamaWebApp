


from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import config_file as cf

app = Flask(__name__)
app.config['SECRET_KEY'] = cf.WTF_KEY

tbg_query_index = None

class QueryForm(FlaskForm):
    query_string = StringField('Enter your question here:', validators=[DataRequired()])
    submit = SubmitField('Query')

def load_index():
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if tbg_query_index is None:
        load_index()

    query_text = None
    query_response = ''

    q_form = QueryForm()

    if q_form.validate_on_submit():
        query_text = q_form.query_string.data

        query_response = '' # TODO: Function call here

    return render_template('index.html', form=q_form, query_response=query_response)
