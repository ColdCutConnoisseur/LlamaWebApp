"""TBG Darwin OpenAI / Llamaindex website"""

from flask import Flask, render_template, url_for, session, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from flask_bootstrap import Bootstrap

import config_file as cf
from index_helpers import load_index, combine_pangolin_indices

app = Flask(__name__)
app.config['SECRET_KEY'] = cf.WTF_KEY

bootstrap = Bootstrap(app)

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
def check_login_page():

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

        return render_template('login.html', form=login_form)


@app.route('/', methods=['GET', 'POST'])
def index():

    user_logged_in = check_login_state(session)
    
    if user_logged_in:
        loaded_index = load_index("/new_index_storage_folder") # CONSIDER: Either load each time or set as 'session' object

        query_text = None
        query_response = ''

        q_form = QueryForm()

        if q_form.validate_on_submit():
            query_text = q_form.query_string.data

            if loaded_index: # Filter out bad index loads (which will return 'None')
                query_engine = loaded_index.as_query_engine()
                query_response = query_engine.query(query_text)

        return render_template('index.html', form=q_form, query_response=query_response)
    
    else:
        return redirect('/login')

@app.route('/pangolin', methods=['GET', 'POST'])
def pangolin_query():

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
                                storage_folder19
                                )

    query_text = None
    query_response = ''

    q_form = QueryForm()

    if q_form.validate_on_submit():
        query_text = q_form.query_string.data

        if loaded_index: # Filter out bad index loads (which will return 'None')
            query_engine = loaded_index.as_query_engine()

            query_prompt = f"The 'user query' is '{query_text}'."+\
                           "  If the information required to respond to the 'user query'"+\
                           " is not found within 'chunk1' through 'chunk19',"+\
                           "then return 'not found' as a response." +\
                           "  Prioritize specific information from the listed 'chunks'"+\
                           " and respond to the 'user query' without including any information"+\
                           " that is not directly being asked by the 'user query'."
            
            query_response = query_engine.query(query_prompt)

    return render_template('pangolin.html', form=q_form, query_response=query_response)
