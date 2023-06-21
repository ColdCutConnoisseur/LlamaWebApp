"""TBG Darwin OpenAI / Llamaindex website"""

import time
from threading import Thread

from flask import Flask, render_template, url_for, session, redirect, flash, request, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from flask_bootstrap import Bootstrap

from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

import config_file as cf
from index_helpers import load_index, combine_pangolin_indices


app = Flask(__name__)
app.config['SECRET_KEY'] = cf.WTF_KEY

bootstrap = Bootstrap(app)
Mobility(app)

P_HASH_CHECK = cf.PW_HASH

class QueryForm(FlaskForm):
    query_string = StringField('Enter your question here:', validators=[DataRequired()])
    submit = SubmitField('Query')

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


def check_login_state(session_obj):
    """Helper"""
    try:
        current_state = session_obj['UserSignedIn']

    except KeyError:
        session_obj['UserSignedIn'] = False
        current_state = session_obj['UserSignedIn']

    return current_state

    

@app.route('/login', methods=['GET', 'POST'])
@mobile_template('{mobile/}login.html')
def check_login_page(template):

    user_logged_in = check_login_state(session)

    if user_logged_in:
        return redirect('/')
    
    else:
        login_form = LoginForm()

        if login_form.validate_on_submit():
            pword = login_form.password.data

            session['UserSignedIn'] = check_password_hash(P_HASH_CHECK, pword)

            if session['UserSignedIn']:
                return redirect('/')
            
            else:
                flash('Invalid password!')

        return render_template(template, form=login_form)


@app.route('/', methods=['GET', 'POST'])
@mobile_template('{mobile/}index.html')
def index(template):

    user_logged_in = check_login_state(session)
    
    if user_logged_in:
        loaded_index = load_index("/new_index_storage_folder")

        query_text = None
        query_response = ''

        q_form = QueryForm()

        if q_form.validate_on_submit():
            query_text = q_form.query_string.data

            if loaded_index: # Filter out bad index loads (which will return 'None')
                query_engine = loaded_index.as_query_engine()
                query_response = query_engine.query(query_text)

        return render_template(template, form=q_form, query_response=query_response)
    
    else:
        return redirect('/login')

def load_pangolin_resources():
    storage_folder1 = "/pangolin_index_storage_folder1"
    storage_folder2 = "/pangolin_index_storage_folder2"
    storage_folder3 = "/pangolin_index_storage_folder3"
    storage_folder4 = "/pangolin_index_storage_folder4"
    storage_folder5 = "/pangolin_index_storage_folder5"
    storage_folder6 = "/pangolin_index_storage_folder6"
    storage_folder7 = "/pangolin_index_storage_folder7"
    storage_folder8 = "/pangolin_index_storage_folder8"
    storage_folder9 = "/pangolin_index_storage_folder9"
    storage_folder10 = "/pangolin_index_storage_folder10"
    storage_folder11 = "/pangolin_index_storage_folder11"
    storage_folder12 = "/pangolin_index_storage_folder12"
    storage_folder13 = "/pangolin_index_storage_folder13"
    storage_folder14 = "/pangolin_index_storage_folder14"
    storage_folder15 = "/pangolin_index_storage_folder15"
    storage_folder16 = "/pangolin_index_storage_folder16"
    storage_folder17 = "/pangolin_index_storage_folder17"
    storage_folder18 = "/pangolin_index_storage_folder18"
    storage_folder19 = "/pangolin_index_storage_folder19"
    storage_folder20 = "/pangolin_index_storage_folder20"
    storage_folder21 = "/pangolin_index_storage_folder21"
    storage_folder22 = "/pangolin_index_storage_folder22"
    storage_folder23 = "/pangolin_index_storage_folder23"
    storage_folder24 = "/pangolin_index_storage_folder24"
    storage_folder25 = "/pangolin_index_storage_folder25"
    storage_folder26 = "/pangolin_index_storage_folder26"

    loaded_index = combine_pangolin_indices(
                                storage_folder1,
                                storage_folder2,
                                storage_folder3,
                                storage_folder4,
                                storage_folder5,
                                storage_folder6,
                                storage_folder7,
                                storage_folder8,
                                storage_folder9,
                                storage_folder10,
                                storage_folder11,
                                storage_folder12,
                                storage_folder13,
                                storage_folder14,
                                storage_folder15,
                                storage_folder16,
                                storage_folder17,
                                storage_folder18,
                                storage_folder19,
                                storage_folder20,
                                storage_folder21,
                                storage_folder22,
                                storage_folder23,
                                storage_folder24,
                                storage_folder25,
                                storage_folder26
                                )
    return loaded_index


@app.route('/pangolin')
@mobile_template('{mobile/}loading.html')
def pangolin_query(template):
    return render_template(template)

@app.route('/load_pangolin_index')
def old_load():
    return "Finished!"

@app.route('/pangolin_loaded', methods=['GET', 'POST'])
@mobile_template('{mobile/}pangolin.html')
def load_pangolin_index(template):
    p_index = load_pangolin_resources()
    query_text = None
    query_response = ''

    q_form = QueryForm()

    if q_form.validate_on_submit():
        query_text = q_form.query_string.data

        if p_index: # Filter out bad index loads (which will return 'None')
            print("Index exists!")
            query_engine = p_index.as_query_engine()

            query_prompt_prev = f"The 'user query' is '{query_text}'."+\
                        "  If the information required to respond to the 'user query'"+\
                        " is not found within 'chunk1' through 'chunk26',"+\
                        "then return 'not found' as a response." +\
                        "  Prioritize specific information from the listed 'chunks'"+\
                        " and respond to the 'user query' without including any information"+\
                        " that is not directly being asked by the 'user query'."
            
            query_prompt = f"The 'user query' is '{query_text}'."+\
                            " Please only respond to the 'user query' with information" +\
                            " found only in the provided 'chunks', 'chunk1' to 'chunk26'.  If the information" +\
                            " is not found within those 'chunks' then respond with" +\
                            " 'not found'."
            
            query_response = query_engine.query(query_prompt)

    return render_template(template, form=q_form, query_response=query_response)
