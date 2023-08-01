"""TBG Darwin OpenAI / Llamaindex website"""

import time
import io
from threading import Thread

from flask import Flask, render_template, url_for, session, redirect, flash, request, g, Response, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from flask_bootstrap import Bootstrap
#import requests
#from lxml import etree

from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

import config_file as cf
from index_helpers import load_index, combine_pangolin_indices, combine_darwin_indices


app = Flask(__name__)
app.config['SECRET_KEY'] = cf.WTF_KEY

bootstrap = Bootstrap(app)
Mobility(app)

P_HASH_CHECK = cf.PW_HASH

class QueryForm(FlaskForm):
    query_string = StringField('Enter your question here:', validators=[DataRequired()])
    submit = SubmitField('Query')

class LoginForm(FlaskForm):
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

def load_darwin_resources():
    storage_folder1 = "/darwin_indices/darwin11_13"
    storage_folder2 = "/darwin_indices/darwin7_42"
    storage_folder3 = "/darwin_indices/darwin21_24"
    storage_folder4 = "/darwin_indices/darwin12_34"
    storage_folder5 = "/darwin_indices/darwin15_23"
    storage_folder6 = "/darwin_indices/darwin8_35"
    storage_folder7 = "/darwin_indices/darwin21_4"
    storage_folder8 = "/darwin_indices/darwin15_24"
    storage_folder9 = "/darwin_indices/darwin21_23"
    storage_folder10 = "/darwin_indices/darwin12_33"
    storage_folder11 = "/darwin_indices/darwin11_14"
    storage_folder12 = "/darwin_indices/darwin21_3"
    storage_folder13 = "/darwin_indices/darwin8_32"
    storage_folder14 = "/darwin_indices/darwin15_12"
    storage_folder15 = "/darwin_indices/darwin21_15"
    storage_folder16 = "/darwin_indices/darwin11_22"
    storage_folder17 = "/darwin_indices/darwin11_25"
    storage_folder18 = "/darwin_indices/darwin16_32"
    storage_folder19 = "/darwin_indices/darwin21_12"
    storage_folder20 = "/darwin_indices/darwin15_15"
    storage_folder21 = "/darwin_indices/darwin19_11"
    storage_folder22 = "/darwin_indices/darwin4_38"
    storage_folder23 = "/darwin_indices/darwin7_20"
    storage_folder24 = "/darwin_indices/darwin3_10"
    storage_folder25 = "/darwin_indices/darwin15_41"
    storage_folder26 = "/darwin_indices/darwin3_28"
    storage_folder27 = "/darwin_indices/darwin7_18"
    storage_folder28 = "/darwin_indices/darwin3_17"
    storage_folder29 = "/darwin_indices/darwin19_29"
    storage_folder30 = "/darwin_indices/darwin7_27"
    storage_folder31 = "/darwin_indices/darwin19_20"
    storage_folder32 = "/darwin_indices/darwin4_36"
    storage_folder33 = "/darwin_indices/darwin3_21"
    storage_folder34 = "/darwin_indices/darwin7_11"
    storage_folder35 = "/darwin_indices/darwin7_29"
    storage_folder36 = "/darwin_indices/darwin19_27"
    storage_folder37 = "/darwin_indices/darwin3_19"
    storage_folder38 = "/darwin_indices/darwin19_18"
    storage_folder39 = "/darwin_indices/darwin7_16"
    storage_folder40 = "/darwin_indices/darwin3_26"
    storage_folder41 = "/darwin_indices/darwin4_31"
    storage_folder42 = "/darwin_indices/darwin15_14"
    storage_folder43 = "/darwin_indices/darwin21_13"
    storage_folder44 = "/darwin_indices/darwin11_24"
    storage_folder45 = "/darwin_indices/darwin11_23"
    storage_folder46 = "/darwin_indices/darwin21_14"
    storage_folder47 = "/darwin_indices/darwin15_13"
    storage_folder48 = "/darwin_indices/darwin11_15"
    storage_folder49 = "/darwin_indices/darwin21_22"
    storage_folder50 = "/darwin_indices/darwin12_32"
    storage_folder51 = "/darwin_indices/darwin15_25"
    storage_folder52 = "/darwin_indices/darwin8_33"
    storage_folder53 = "/darwin_indices/darwin21_2"
    storage_folder54 = "/darwin_indices/darwin15_22"
    storage_folder55 = "/darwin_indices/darwin21_25"
    storage_folder56 = "/darwin_indices/darwin12_35"
    storage_folder57 = "/darwin_indices/darwin7_43"
    storage_folder58 = "/darwin_indices/darwin21_5"
    storage_folder59 = "/darwin_indices/darwin8_34"
    storage_folder60 = "/darwin_indices/darwin7_28"
    storage_folder61 = "/darwin_indices/darwin19_26"
    storage_folder62 = "/darwin_indices/darwin4_30"
    storage_folder63 = "/darwin_indices/darwin3_27"
    storage_folder64 = "/darwin_indices/darwin19_19"
    storage_folder65 = "/darwin_indices/darwin7_17"
    storage_folder66 = "/darwin_indices/darwin7_10"
    storage_folder67 = "/darwin_indices/darwin3_20"
    storage_folder68 = "/darwin_indices/darwin4_37"
    storage_folder69 = "/darwin_indices/darwin7_19"
    storage_folder70 = "/darwin_indices/darwin19_17"
    storage_folder71 = "/darwin_indices/darwin3_29"
    storage_folder72 = "/darwin_indices/darwin19_28"
    storage_folder73 = "/darwin_indices/darwin7_26"
    storage_folder74 = "/darwin_indices/darwin3_16"
    storage_folder75 = "/darwin_indices/darwin4_39"
    storage_folder76 = "/darwin_indices/darwin19_10"
    storage_folder77 = "/darwin_indices/darwin3_11"
    storage_folder78 = "/darwin_indices/darwin15_40"
    storage_folder79 = "/darwin_indices/darwin7_21"
    storage_folder80 = "/darwin_indices/darwin14_14"
    storage_folder81 = "/darwin_indices/darwin10_24"
    storage_folder82 = "/darwin_indices/darwin10_23"
    storage_folder83 = "/darwin_indices/darwin14_13"
    storage_folder84 = "/darwin_indices/darwin9_9"
    storage_folder85 = "/darwin_indices/darwin3_7"
    storage_folder86 = "/darwin_indices/darwin12_7"
    storage_folder87 = "/darwin_indices/darwin6_44"
    storage_folder88 = "/darwin_indices/darwin10_15"
    storage_folder89 = "/darwin_indices/darwin14_25"
    storage_folder90 = "/darwin_indices/darwin13_32"
    storage_folder91 = "/darwin_indices/darwin20_22"
    storage_folder92 = "/darwin_indices/darwin1_3"
    storage_folder93 = "/darwin_indices/darwin9_33"
    storage_folder94 = "/darwin_indices/darwin10_3"
    storage_folder95 = "/darwin_indices/darwin13_35"
    storage_folder96 = "/darwin_indices/darwin20_25"
    storage_folder97 = "/darwin_indices/darwin14_22"
    storage_folder98 = "/darwin_indices/.DS_Store"
    storage_folder99 = "/darwin_indices/darwin12_9"
    storage_folder100 = "/darwin_indices/darwin10_12"
    storage_folder101 = "/darwin_indices/darwin6_43"
    storage_folder102 = "/darwin_indices/darwin9_7"
    storage_folder103 = "/darwin_indices/darwin3_9"
    storage_folder104 = "/darwin_indices/darwin10_4"
    storage_folder105 = "/darwin_indices/darwin1_4"
    storage_folder106 = "/darwin_indices/darwin9_34"
    storage_folder107 = "/darwin_indices/darwin2_18"
    storage_folder108 = "/darwin_indices/darwin16_6"
    storage_folder109 = "/darwin_indices/darwin6_28"
    storage_folder110 = "/darwin_indices/darwin7_6"
    storage_folder111 = "/darwin_indices/darwin18_26"
    storage_folder112 = "/darwin_indices/darwin2_27"
    storage_folder113 = "/darwin_indices/darwin5_30"
    storage_folder114 = "/darwin_indices/darwin18_19"
    storage_folder115 = "/darwin_indices/darwin6_17"
    storage_folder116 = "/darwin_indices/darwin18_21"
    storage_folder117 = "/darwin_indices/darwin7_1"
    storage_folder118 = "/darwin_indices/darwin16_1"
    storage_folder119 = "/darwin_indices/darwin6_10"
    storage_folder120 = "/darwin_indices/darwin10_41"
    storage_folder121 = "/darwin_indices/darwin2_20"
    storage_folder122 = "/darwin_indices/darwin6_19"
    storage_folder123 = "/darwin_indices/darwin5_5"
    storage_folder124 = "/darwin_indices/darwin18_17"
    storage_folder125 = "/darwin_indices/darwin2_29"
    storage_folder126 = "/darwin_indices/darwin14_5"
    storage_folder127 = "/darwin_indices/darwin7_8"
    storage_folder128 = "/darwin_indices/darwin18_28"
    storage_folder129 = "/darwin_indices/darwin6_26"
    storage_folder130 = "/darwin_indices/darwin1_31"
    storage_folder131 = "/darwin_indices/darwin20_40"
    storage_folder132 = "/darwin_indices/darwin16_8"
    storage_folder133 = "/darwin_indices/darwin2_16"
    storage_folder134 = "/darwin_indices/darwin14_2"
    storage_folder135 = "/darwin_indices/darwin5_2"
    storage_folder136 = "/darwin_indices/darwin18_10"
    storage_folder137 = "/darwin_indices/darwin2_11"
    storage_folder138 = "/darwin_indices/darwin14_40"
    storage_folder139 = "/darwin_indices/darwin6_21"
    storage_folder140 = "/darwin_indices/darwin10_13"
    storage_folder141 = "/darwin_indices/darwin3_8"
    storage_folder142 = "/darwin_indices/darwin6_42"
    storage_folder143 = "/darwin_indices/darwin9_6"
    storage_folder144 = "/darwin_indices/darwin14_23"
    storage_folder145 = "/darwin_indices/darwin13_34"
    storage_folder146 = "/darwin_indices/darwin20_24"
    storage_folder147 = "/darwin_indices/darwin18_6"
    storage_folder148 = "/darwin_indices/darwin12_8"
    storage_folder149 = "/darwin_indices/darwin1_5"
    storage_folder150 = "/darwin_indices/darwin9_35"
    storage_folder151 = "/darwin_indices/darwin10_5"
    storage_folder152 = "/darwin_indices/darwin18_1"
    storage_folder153 = "/darwin_indices/darwin13_33"
    storage_folder154 = "/darwin_indices/darwin20_23"
    storage_folder155 = "/darwin_indices/darwin14_24"
    storage_folder156 = "/darwin_indices/darwin9_1"
    storage_folder157 = "/darwin_indices/darwin10_14"
    storage_folder158 = "/darwin_indices/darwin10_2"
    storage_folder159 = "/darwin_indices/darwin1_2"
    storage_folder160 = "/darwin_indices/darwin9_32"
    storage_folder161 = "/darwin_indices/darwin20_15"
    storage_folder162 = "/darwin_indices/darwin14_12"
    storage_folder163 = "/darwin_indices/darwin10_22"
    storage_folder164 = "/darwin_indices/darwin17_35"
    storage_folder165 = "/darwin_indices/darwin12_6"
    storage_folder166 = "/darwin_indices/darwin3_6"
    storage_folder167 = "/darwin_indices/darwin9_8"
    storage_folder168 = "/darwin_indices/darwin17_32"
    storage_folder169 = "/darwin_indices/darwin10_25"
    storage_folder170 = "/darwin_indices/darwin14_15"
    storage_folder171 = "/darwin_indices/darwin20_12"
    storage_folder172 = "/darwin_indices/darwin3_1"
    storage_folder173 = "/darwin_indices/darwin5_3"
    storage_folder174 = "/darwin_indices/darwin18_11"
    storage_folder175 = "/darwin_indices/darwin14_3"
    storage_folder176 = "/darwin_indices/darwin6_20"
    storage_folder177 = "/darwin_indices/darwin2_10"
    storage_folder178 = "/darwin_indices/darwin14_41"
    storage_folder179 = "/darwin_indices/darwin2_28"
    storage_folder180 = "/darwin_indices/darwin14_4"
    storage_folder181 = "/darwin_indices/darwin6_18"
    storage_folder182 = "/darwin_indices/darwin5_4"
    storage_folder183 = "/darwin_indices/darwin18_16"
    storage_folder184 = "/darwin_indices/darwin16_9"
    storage_folder185 = "/darwin_indices/darwin2_17"
    storage_folder186 = "/darwin_indices/darwin18_29"
    storage_folder187 = "/darwin_indices/darwin7_9"
    storage_folder188 = "/darwin_indices/darwin1_30"
    storage_folder189 = "/darwin_indices/darwin6_27"
    storage_folder190 = "/darwin_indices/darwin18_20"
    storage_folder191 = "/darwin_indices/darwin2_21"
    storage_folder192 = "/darwin_indices/darwin6_11"
    storage_folder193 = "/darwin_indices/darwin10_40"
    storage_folder194 = "/darwin_indices/darwin6_29"
    storage_folder195 = "/darwin_indices/darwin18_27"
    storage_folder196 = "/darwin_indices/darwin7_7"
    storage_folder197 = "/darwin_indices/darwin2_19"
    storage_folder198 = "/darwin_indices/darwin16_7"
    storage_folder199 = "/darwin_indices/darwin18_18"
    storage_folder200 = "/darwin_indices/darwin6_16"
    storage_folder201 = "/darwin_indices/darwin5_31"
    storage_folder202 = "/darwin_indices/darwin2_26"
    storage_folder203 = "/darwin_indices/darwin1_23"
    storage_folder204 = "/darwin_indices/darwin6_34"
    storage_folder205 = "/darwin_indices/darwin5_13"
    storage_folder206 = "/darwin_indices/darwin5_14"
    storage_folder207 = "/darwin_indices/darwin6_33"
    storage_folder208 = "/darwin_indices/darwin1_24"
    storage_folder209 = "/darwin_indices/darwin5_22"
    storage_folder210 = "/darwin_indices/darwin1_12"
    storage_folder211 = "/darwin_indices/darwin18_34"
    storage_folder212 = "/darwin_indices/darwin1_15"
    storage_folder213 = "/darwin_indices/darwin2_32"
    storage_folder214 = "/darwin_indices/darwin5_25"
    storage_folder215 = "/darwin_indices/darwin18_33"
    storage_folder216 = "/darwin_indices/darwin9_21"
    storage_folder217 = "/darwin_indices/darwin10_38"
    storage_folder218 = "/darwin_indices/darwin20_30"
    storage_folder219 = "/darwin_indices/darwin13_20"
    storage_folder220 = "/darwin_indices/darwin14_37"
    storage_folder221 = "/darwin_indices/darwin13_18"
    storage_folder222 = "/darwin_indices/darwin17_28"
    storage_folder223 = "/darwin_indices/darwin9_26"
    storage_folder224 = "/darwin_indices/darwin14_30"
    storage_folder225 = "/darwin_indices/darwin20_37"
    storage_folder226 = "/darwin_indices/darwin13_27"
    storage_folder227 = "/darwin_indices/darwin9_19"
    storage_folder228 = "/darwin_indices/darwin17_17"
    storage_folder229 = "/darwin_indices/darwin14_39"
    storage_folder230 = "/darwin_indices/darwin9_10"
    storage_folder231 = "/darwin_indices/darwin20_7"
    storage_folder232 = "/darwin_indices/darwin13_11"
    storage_folder233 = "/darwin_indices/darwin17_21"
    storage_folder234 = "/darwin_indices/darwin10_36"
    storage_folder235 = "/darwin_indices/darwin17_19"
    storage_folder236 = "/darwin_indices/darwin9_17"
    storage_folder237 = "/darwin_indices/darwin20_39"
    storage_folder238 = "/darwin_indices/darwin13_29"
    storage_folder239 = "/darwin_indices/darwin9_28"
    storage_folder240 = "/darwin_indices/darwin10_31"
    storage_folder241 = "/darwin_indices/darwin17_26"
    storage_folder242 = "/darwin_indices/darwin13_16"
    storage_folder243 = "/darwin_indices/darwin5_24"
    storage_folder244 = "/darwin_indices/darwin1_14"
    storage_folder245 = "/darwin_indices/darwin18_32"
    storage_folder246 = "/darwin_indices/darwin1_13"
    storage_folder247 = "/darwin_indices/darwin5_23"
    storage_folder248 = "/darwin_indices/darwin18_35"
    storage_folder249 = "/darwin_indices/darwin1_25"
    storage_folder250 = "/darwin_indices/darwin6_32"
    storage_folder251 = "/darwin_indices/darwin5_15"
    storage_folder252 = "/darwin_indices/darwin5_12"
    storage_folder253 = "/darwin_indices/darwin6_35"
    storage_folder254 = "/darwin_indices/darwin1_22"
    storage_folder255 = "/darwin_indices/darwin20_38"
    storage_folder256 = "/darwin_indices/darwin13_28"
    storage_folder257 = "/darwin_indices/darwin17_18"
    storage_folder258 = "/darwin_indices/darwin9_16"
    storage_folder259 = "/darwin_indices/darwin20_1"
    storage_folder260 = "/darwin_indices/darwin13_17"
    storage_folder261 = "/darwin_indices/darwin9_29"
    storage_folder262 = "/darwin_indices/darwin17_27"
    storage_folder263 = "/darwin_indices/darwin10_30"
    storage_folder264 = "/darwin_indices/darwin9_11"
    storage_folder265 = "/darwin_indices/darwin14_38"
    storage_folder266 = "/darwin_indices/darwin10_37"
    storage_folder267 = "/darwin_indices/darwin17_20"
    storage_folder268 = "/darwin_indices/darwin13_10"
    storage_folder269 = "/darwin_indices/darwin17_29"
    storage_folder270 = "/darwin_indices/darwin9_27"
    storage_folder271 = "/darwin_indices/darwin13_19"
    storage_folder272 = "/darwin_indices/darwin9_18"
    storage_folder273 = "/darwin_indices/darwin17_16"
    storage_folder274 = "/darwin_indices/darwin20_36"
    storage_folder275 = "/darwin_indices/darwin13_26"
    storage_folder276 = "/darwin_indices/darwin14_31"
    storage_folder277 = "/darwin_indices/darwin9_20"
    storage_folder278 = "/darwin_indices/darwin10_39"
    storage_folder279 = "/darwin_indices/darwin14_36"
    storage_folder280 = "/darwin_indices/darwin20_31"
    storage_folder281 = "/darwin_indices/darwin13_21"
    storage_folder282 = "/darwin_indices/darwin17_11"
    storage_folder283 = "/darwin_indices/darwin20_8"
    storage_folder284 = "/darwin_indices/darwin3_33"
    storage_folder285 = "/darwin_indices/darwin4_24"
    storage_folder286 = "/darwin_indices/darwin4_6"
    storage_folder287 = "/darwin_indices/darwin15_6"
    storage_folder288 = "/darwin_indices/darwin19_32"
    storage_folder289 = "/darwin_indices/darwin4_23"
    storage_folder290 = "/darwin_indices/darwin3_34"
    storage_folder291 = "/darwin_indices/darwin19_35"
    storage_folder292 = "/darwin_indices/darwin15_1"
    storage_folder293 = "/darwin_indices/darwin4_1"
    storage_folder294 = "/darwin_indices/darwin7_32"
    storage_folder295 = "/darwin_indices/darwin4_15"
    storage_folder296 = "/darwin_indices/darwin4_8"
    storage_folder297 = "/darwin_indices/darwin17_5"
    storage_folder298 = "/darwin_indices/darwin6_5"
    storage_folder299 = "/darwin_indices/darwin4_12"
    storage_folder300 = "/darwin_indices/darwin7_35"
    storage_folder301 = "/darwin_indices/darwin6_2"
    storage_folder302 = "/darwin_indices/darwin17_2"
    storage_folder303 = "/darwin_indices/darwin12_28"
    storage_folder304 = "/darwin_indices/darwin21_38"
    storage_folder305 = "/darwin_indices/darwin16_18"
    storage_folder306 = "/darwin_indices/darwin8_16"
    storage_folder307 = "/darwin_indices/darwin4_46"
    storage_folder308 = "/darwin_indices/darwin8_3"
    storage_folder309 = "/darwin_indices/darwin12_17"
    storage_folder310 = "/darwin_indices/darwin8_29"
    storage_folder311 = "/darwin_indices/darwin11_30"
    storage_folder312 = "/darwin_indices/darwin16_27"
    storage_folder313 = "/darwin_indices/darwin8_11"
    storage_folder314 = "/darwin_indices/darwin11_7"
    storage_folder315 = "/darwin_indices/darwin15_38"
    storage_folder316 = "/darwin_indices/darwin19_4"
    storage_folder317 = "/darwin_indices/darwin16_20"
    storage_folder318 = "/darwin_indices/darwin11_37"
    storage_folder319 = "/darwin_indices/darwin12_10"
    storage_folder320 = "/darwin_indices/darwin4_41"
    storage_folder321 = "/darwin_indices/darwin13_3"
    storage_folder322 = "/darwin_indices/darwin16_29"
    storage_folder323 = "/darwin_indices/darwin8_27"
    storage_folder324 = "/darwin_indices/darwin12_19"
    storage_folder325 = "/darwin_indices/darwin2_3"
    storage_folder326 = "/darwin_indices/darwin8_18"
    storage_folder327 = "/darwin_indices/darwin16_16"
    storage_folder328 = "/darwin_indices/darwin15_31"
    storage_folder329 = "/darwin_indices/darwin12_26"
    storage_folder330 = "/darwin_indices/darwin21_36"
    storage_folder331 = "/darwin_indices/darwin2_4"
    storage_folder332 = "/darwin_indices/darwin8_20"
    storage_folder333 = "/darwin_indices/darwin13_4"
    storage_folder334 = "/darwin_indices/darwin12_21"
    storage_folder335 = "/darwin_indices/darwin21_31"
    storage_folder336 = "/darwin_indices/darwin15_36"
    storage_folder337 = "/darwin_indices/darwin16_11"
    storage_folder338 = "/darwin_indices/darwin11_9"
    storage_folder339 = "/darwin_indices/darwin7_34"
    storage_folder340 = "/darwin_indices/darwin4_13"
    storage_folder341 = "/darwin_indices/darwin17_3"
    storage_folder342 = "/darwin_indices/darwin6_3"
    storage_folder343 = "/darwin_indices/darwin4_9"
    storage_folder344 = "/darwin_indices/darwin4_14"
    storage_folder345 = "/darwin_indices/darwin7_33"
    storage_folder346 = "/darwin_indices/darwin6_4"
    storage_folder347 = "/darwin_indices/darwin17_4"
    storage_folder348 = "/darwin_indices/darwin3_35"
    storage_folder349 = "/darwin_indices/darwin4_22"
    storage_folder350 = "/darwin_indices/darwin19_34"
    storage_folder351 = "/darwin_indices/darwin4_25"
    storage_folder352 = "/darwin_indices/darwin3_32"
    storage_folder353 = "/darwin_indices/darwin15_7"
    storage_folder354 = "/darwin_indices/darwin19_33"
    storage_folder355 = "/darwin_indices/darwin4_7"
    storage_folder356 = "/darwin_indices/darwin8_21"
    storage_folder357 = "/darwin_indices/darwin13_5"
    storage_folder358 = "/darwin_indices/darwin2_5"
    storage_folder359 = "/darwin_indices/darwin11_8"
    storage_folder360 = "/darwin_indices/darwin15_37"
    storage_folder361 = "/darwin_indices/darwin12_20"
    storage_folder362 = "/darwin_indices/darwin21_30"
    storage_folder363 = "/darwin_indices/darwin2_2"
    storage_folder364 = "/darwin_indices/darwin12_18"
    storage_folder365 = "/darwin_indices/darwin16_28"
    storage_folder366 = "/darwin_indices/darwin13_2"
    storage_folder367 = "/darwin_indices/darwin8_26"
    storage_folder368 = "/darwin_indices/darwin12_27"
    storage_folder369 = "/darwin_indices/darwin21_37"
    storage_folder370 = "/darwin_indices/darwin15_30"
    storage_folder371 = "/darwin_indices/darwin8_19"
    storage_folder372 = "/darwin_indices/darwin16_17"
    storage_folder373 = "/darwin_indices/darwin15_39"
    storage_folder374 = "/darwin_indices/darwin8_10"
    storage_folder375 = "/darwin_indices/darwin11_6"
    storage_folder376 = "/darwin_indices/darwin8_5"
    storage_folder377 = "/darwin_indices/darwin12_11"
    storage_folder378 = "/darwin_indices/darwin4_40"
    storage_folder379 = "/darwin_indices/darwin11_36"
    storage_folder380 = "/darwin_indices/darwin19_5"
    storage_folder381 = "/darwin_indices/darwin16_21"
    storage_folder382 = "/darwin_indices/darwin16_19"
    storage_folder383 = "/darwin_indices/darwin11_1"
    storage_folder384 = "/darwin_indices/darwin8_17"
    storage_folder385 = "/darwin_indices/darwin12_29"
    storage_folder386 = "/darwin_indices/darwin21_39"
    storage_folder387 = "/darwin_indices/darwin8_28"
    storage_folder388 = "/darwin_indices/darwin16_26"
    storage_folder389 = "/darwin_indices/darwin11_31"
    storage_folder390 = "/darwin_indices/darwin4_47"
    storage_folder391 = "/darwin_indices/darwin8_2"
    storage_folder392 = "/darwin_indices/darwin12_16"
    storage_folder393 = "/darwin_indices/darwin3_14"
    storage_folder394 = "/darwin_indices/darwin7_24"
    storage_folder395 = "/darwin_indices/darwin19_12"
    storage_folder396 = "/darwin_indices/darwin7_23"
    storage_folder397 = "/darwin_indices/darwin3_13"
    storage_folder398 = "/darwin_indices/darwin15_42"
    storage_folder399 = "/darwin_indices/darwin19_24"
    storage_folder400 = "/darwin_indices/darwin7_15"
    storage_folder401 = "/darwin_indices/darwin4_32"
    storage_folder402 = "/darwin_indices/darwin3_25"
    storage_folder403 = "/darwin_indices/darwin19_23"
    storage_folder404 = "/darwin_indices/darwin3_22"
    storage_folder405 = "/darwin_indices/darwin4_35"
    storage_folder406 = "/darwin_indices/darwin7_12"
    storage_folder407 = "/darwin_indices/darwin21_20"
    storage_folder408 = "/darwin_indices/darwin12_30"
    storage_folder409 = "/darwin_indices/darwin15_27"
    storage_folder410 = "/darwin_indices/darwin11_17"
    storage_folder411 = "/darwin_indices/darwin15_18"
    storage_folder412 = "/darwin_indices/darwin11_28"
    storage_folder413 = "/darwin_indices/darwin8_31"
    storage_folder414 = "/darwin_indices/darwin11_10"
    storage_folder415 = "/darwin_indices/darwin7_41"
    storage_folder416 = "/darwin_indices/darwin15_20"
    storage_folder417 = "/darwin_indices/darwin21_27"
    storage_folder418 = "/darwin_indices/darwin12_37"
    storage_folder419 = "/darwin_indices/darwin8_36"
    storage_folder420 = "/darwin_indices/darwin21_18"
    storage_folder421 = "/darwin_indices/darwin21_7"
    storage_folder422 = "/darwin_indices/darwin16_31"
    storage_folder423 = "/darwin_indices/darwin11_26"
    storage_folder424 = "/darwin_indices/darwin15_16"
    storage_folder425 = "/darwin_indices/darwin21_11"
    storage_folder426 = "/darwin_indices/darwin11_19"
    storage_folder427 = "/darwin_indices/darwin15_29"
    storage_folder428 = "/darwin_indices/darwin21_16"
    storage_folder429 = "/darwin_indices/darwin15_11"
    storage_folder430 = "/darwin_indices/darwin21_9"
    storage_folder431 = "/darwin_indices/darwin11_21"
    storage_folder432 = "/darwin_indices/darwin8_38"
    storage_folder433 = "/darwin_indices/darwin21_29"
    storage_folder434 = "/darwin_indices/darwin12_39"
    storage_folder435 = "/darwin_indices/darwin19_22"
    storage_folder436 = "/darwin_indices/darwin7_13"
    storage_folder437 = "/darwin_indices/darwin4_34"
    storage_folder438 = "/darwin_indices/darwin3_23"
    storage_folder439 = "/darwin_indices/darwin19_25"
    storage_folder440 = "/darwin_indices/darwin3_24"
    storage_folder441 = "/darwin_indices/darwin4_33"
    storage_folder442 = "/darwin_indices/darwin7_14"
    storage_folder443 = "/darwin_indices/darwin19_13"
    storage_folder444 = "/darwin_indices/darwin3_12"
    storage_folder445 = "/darwin_indices/darwin15_43"
    storage_folder446 = "/darwin_indices/darwin7_22"
    storage_folder447 = "/darwin_indices/darwin19_14"
    storage_folder448 = "/darwin_indices/darwin7_25"
    storage_folder449 = "/darwin_indices/darwin15_44"
    storage_folder450 = "/darwin_indices/darwin3_15"
    storage_folder451 = "/darwin_indices/darwin11_20"
    storage_folder452 = "/darwin_indices/darwin15_10"
    storage_folder453 = "/darwin_indices/darwin21_8"
    storage_folder454 = "/darwin_indices/darwin21_17"
    storage_folder455 = "/darwin_indices/darwin21_28"
    storage_folder456 = "/darwin_indices/darwin12_38"
    storage_folder457 = "/darwin_indices/darwin21_10"
    storage_folder458 = "/darwin_indices/darwin15_17"
    storage_folder459 = "/darwin_indices/darwin11_27"
    storage_folder460 = "/darwin_indices/darwin16_30"
    storage_folder461 = "/darwin_indices/darwin15_28"
    storage_folder462 = "/darwin_indices/darwin11_18"
    storage_folder463 = "/darwin_indices/darwin21_26"
    storage_folder464 = "/darwin_indices/darwin12_36"
    storage_folder465 = "/darwin_indices/darwin15_21"
    storage_folder466 = "/darwin_indices/darwin11_11"
    storage_folder467 = "/darwin_indices/darwin7_40"
    storage_folder468 = "/darwin_indices/darwin21_6"
    storage_folder469 = "/darwin_indices/darwin21_19"
    storage_folder470 = "/darwin_indices/darwin8_37"
    storage_folder471 = "/darwin_indices/darwin11_16"
    storage_folder472 = "/darwin_indices/darwin15_26"
    storage_folder473 = "/darwin_indices/darwin21_21"
    storage_folder474 = "/darwin_indices/darwin12_31"
    storage_folder475 = "/darwin_indices/darwin11_29"
    storage_folder476 = "/darwin_indices/darwin8_30"
    storage_folder477 = "/darwin_indices/darwin15_19"
    storage_folder478 = "/darwin_indices/darwin21_1"
    storage_folder479 = "/darwin_indices/darwin7_2"
    storage_folder480 = "/darwin_indices/darwin18_22"
    storage_folder481 = "/darwin_indices/darwin16_2"
    storage_folder482 = "/darwin_indices/darwin6_13"
    storage_folder483 = "/darwin_indices/darwin10_42"
    storage_folder484 = "/darwin_indices/darwin2_23"
    storage_folder485 = "/darwin_indices/darwin16_5"
    storage_folder486 = "/darwin_indices/darwin18_25"
    storage_folder487 = "/darwin_indices/darwin7_5"
    storage_folder488 = "/darwin_indices/darwin14_8"
    storage_folder489 = "/darwin_indices/darwin5_33"
    storage_folder490 = "/darwin_indices/darwin2_24"
    storage_folder491 = "/darwin_indices/darwin5_8"
    storage_folder492 = "/darwin_indices/darwin6_14"
    storage_folder493 = "/darwin_indices/darwin14_1"
    storage_folder494 = "/darwin_indices/darwin5_1"
    storage_folder495 = "/darwin_indices/darwin2_12"
    storage_folder496 = "/darwin_indices/darwin14_43"
    storage_folder497 = "/darwin_indices/darwin6_22"
    storage_folder498 = "/darwin_indices/darwin5_6"
    storage_folder499 = "/darwin_indices/darwin18_14"
    storage_folder500 = "/darwin_indices/darwin14_6"
    storage_folder501 = "/darwin_indices/darwin1_32"
    storage_folder502 = "/darwin_indices/darwin6_25"
    storage_folder503 = "/darwin_indices/darwin14_44"
    storage_folder504 = "/darwin_indices/darwin2_15"
    storage_folder505 = "/darwin_indices/darwin10_20"
    storage_folder506 = "/darwin_indices/darwin1_9"
    storage_folder507 = "/darwin_indices/darwin9_39"
    storage_folder508 = "/darwin_indices/darwin20_17"
    storage_folder509 = "/darwin_indices/darwin14_10"
    storage_folder510 = "/darwin_indices/darwin10_9"
    storage_folder511 = "/darwin_indices/darwin3_4"
    storage_folder512 = "/darwin_indices/darwin12_4"
    storage_folder513 = "/darwin_indices/darwin20_28"
    storage_folder514 = "/darwin_indices/darwin14_17"
    storage_folder515 = "/darwin_indices/darwin17_30"
    storage_folder516 = "/darwin_indices/darwin10_27"
    storage_folder517 = "/darwin_indices/darwin14_28"
    storage_folder518 = "/darwin_indices/darwin10_18"
    storage_folder519 = "/darwin_indices/darwin3_3"
    storage_folder520 = "/darwin_indices/darwin14_21"
    storage_folder521 = "/darwin_indices/darwin20_26"
    storage_folder522 = "/darwin_indices/darwin18_4"
    storage_folder523 = "/darwin_indices/darwin10_11"
    storage_folder524 = "/darwin_indices/darwin6_40"
    storage_folder525 = "/darwin_indices/darwin9_4"
    storage_folder526 = "/darwin_indices/darwin10_7"
    storage_folder527 = "/darwin_indices/darwin20_19"
    storage_folder528 = "/darwin_indices/darwin1_7"
    storage_folder529 = "/darwin_indices/darwin9_37"
    storage_folder530 = "/darwin_indices/darwin9_3"
    storage_folder531 = "/darwin_indices/darwin10_16"
    storage_folder532 = "/darwin_indices/darwin18_3"
    storage_folder533 = "/darwin_indices/darwin13_31"
    storage_folder534 = "/darwin_indices/darwin20_21"
    storage_folder535 = "/darwin_indices/darwin14_26"
    storage_folder536 = "/darwin_indices/darwin10_29"
    storage_folder537 = "/darwin_indices/darwin9_30"
    storage_folder538 = "/darwin_indices/darwin14_19"
    storage_folder539 = "/darwin_indices/darwin14_7"
    storage_folder540 = "/darwin_indices/darwin5_7"
    storage_folder541 = "/darwin_indices/darwin18_15"
    storage_folder542 = "/darwin_indices/darwin14_45"
    storage_folder543 = "/darwin_indices/darwin2_14"
    storage_folder544 = "/darwin_indices/darwin6_24"
    storage_folder545 = "/darwin_indices/darwin1_33"
    storage_folder546 = "/darwin_indices/darwin6_23"
    storage_folder547 = "/darwin_indices/darwin2_13"
    storage_folder548 = "/darwin_indices/darwin14_42"
    storage_folder549 = "/darwin_indices/darwin7_4"
    storage_folder550 = "/darwin_indices/darwin18_24"
    storage_folder551 = "/darwin_indices/darwin16_4"
    storage_folder552 = "/darwin_indices/darwin5_9"
    storage_folder553 = "/darwin_indices/darwin10_44"
    storage_folder554 = "/darwin_indices/darwin6_15"
    storage_folder555 = "/darwin_indices/darwin14_9"
    storage_folder556 = "/darwin_indices/darwin2_25"
    storage_folder557 = "/darwin_indices/darwin5_32"
    storage_folder558 = "/darwin_indices/darwin16_3"
    storage_folder559 = "/darwin_indices/darwin18_23"
    storage_folder560 = "/darwin_indices/darwin7_3"
    storage_folder561 = "/darwin_indices/darwin2_22"
    storage_folder562 = "/darwin_indices/darwin6_12"
    storage_folder563 = "/darwin_indices/darwin10_43"
    storage_folder564 = "/darwin_indices/darwin14_27"
    storage_folder565 = "/darwin_indices/darwin13_30"
    storage_folder566 = "/darwin_indices/darwin20_20"
    storage_folder567 = "/darwin_indices/darwin10_17"
    storage_folder568 = "/darwin_indices/darwin14_18"
    storage_folder569 = "/darwin_indices/darwin10_1"
    storage_folder570 = "/darwin_indices/darwin10_28"
    storage_folder571 = "/darwin_indices/darwin9_31"
    storage_folder572 = "/darwin_indices/darwin10_10"
    storage_folder573 = "/darwin_indices/darwin6_41"
    storage_folder574 = "/darwin_indices/darwin9_5"
    storage_folder575 = "/darwin_indices/darwin20_27"
    storage_folder576 = "/darwin_indices/darwin14_20"
    storage_folder577 = "/darwin_indices/darwin18_5"
    storage_folder578 = "/darwin_indices/darwin1_6"
    storage_folder579 = "/darwin_indices/darwin9_36"
    storage_folder580 = "/darwin_indices/darwin10_6"
    storage_folder581 = "/darwin_indices/darwin20_18"
    storage_folder582 = "/darwin_indices/darwin10_26"
    storage_folder583 = "/darwin_indices/darwin17_31"
    storage_folder584 = "/darwin_indices/darwin20_11"
    storage_folder585 = "/darwin_indices/darwin10_19"
    storage_folder586 = "/darwin_indices/darwin3_2"
    storage_folder587 = "/darwin_indices/darwin14_29"
    storage_folder588 = "/darwin_indices/darwin12_2"
    storage_folder589 = "/darwin_indices/darwin14_11"
    storage_folder590 = "/darwin_indices/darwin10_8"
    storage_folder591 = "/darwin_indices/darwin10_21"
    storage_folder592 = "/darwin_indices/darwin1_8"
    storage_folder593 = "/darwin_indices/darwin9_38"
    storage_folder594 = "/darwin_indices/darwin12_5"
    storage_folder595 = "/darwin_indices/darwin20_29"
    storage_folder596 = "/darwin_indices/darwin3_5"
    storage_folder597 = "/darwin_indices/darwin9_25"
    storage_folder598 = "/darwin_indices/darwin20_34"
    storage_folder599 = "/darwin_indices/darwin13_24"
    storage_folder600 = "/darwin_indices/darwin14_33"
    storage_folder601 = "/darwin_indices/darwin17_14"
    storage_folder602 = "/darwin_indices/darwin9_22"
    storage_folder603 = "/darwin_indices/darwin17_13"
    storage_folder604 = "/darwin_indices/darwin14_34"
    storage_folder605 = "/darwin_indices/darwin20_33"
    storage_folder606 = "/darwin_indices/darwin13_23"
    storage_folder607 = "/darwin_indices/darwin9_14"
    storage_folder608 = "/darwin_indices/darwin20_3"
    storage_folder609 = "/darwin_indices/darwin17_25"
    storage_folder610 = "/darwin_indices/darwin10_32"
    storage_folder611 = "/darwin_indices/darwin13_15"
    storage_folder612 = "/darwin_indices/darwin20_4"
    storage_folder613 = "/darwin_indices/darwin9_13"
    storage_folder614 = "/darwin_indices/darwin13_12"
    storage_folder615 = "/darwin_indices/darwin10_35"
    storage_folder616 = "/darwin_indices/darwin17_22"
    storage_folder617 = "/darwin_indices/darwin5_17"
    storage_folder618 = "/darwin_indices/darwin1_27"
    storage_folder619 = "/darwin_indices/darwin6_30"
    storage_folder620 = "/darwin_indices/darwin5_28"
    storage_folder621 = "/darwin_indices/darwin1_18"
    storage_folder622 = "/darwin_indices/darwin6_37"
    storage_folder623 = "/darwin_indices/darwin1_20"
    storage_folder624 = "/darwin_indices/darwin5_10"
    storage_folder625 = "/darwin_indices/darwin9_40"
    storage_folder626 = "/darwin_indices/darwin1_16"
    storage_folder627 = "/darwin_indices/darwin5_26"
    storage_folder628 = "/darwin_indices/darwin2_31"
    storage_folder629 = "/darwin_indices/darwin1_29"
    storage_folder630 = "/darwin_indices/darwin18_30"
    storage_folder631 = "/darwin_indices/darwin5_19"
    storage_folder632 = "/darwin_indices/darwin5_21"
    storage_folder633 = "/darwin_indices/darwin1_11"
    storage_folder634 = "/darwin_indices/darwin18_37"
    storage_folder635 = "/darwin_indices/darwin6_39"
    storage_folder636 = "/darwin_indices/darwin9_12"
    storage_folder637 = "/darwin_indices/darwin20_5"
    storage_folder638 = "/darwin_indices/darwin17_23"
    storage_folder639 = "/darwin_indices/darwin10_34"
    storage_folder640 = "/darwin_indices/darwin13_13"
    storage_folder641 = "/darwin_indices/darwin20_2"
    storage_folder642 = "/darwin_indices/darwin9_15"
    storage_folder643 = "/darwin_indices/darwin13_14"
    storage_folder644 = "/darwin_indices/darwin10_33"
    storage_folder645 = "/darwin_indices/darwin17_24"
    storage_folder646 = "/darwin_indices/darwin9_23"
    storage_folder647 = "/darwin_indices/darwin20_32"
    storage_folder648 = "/darwin_indices/darwin13_22"
    storage_folder649 = "/darwin_indices/darwin14_35"
    storage_folder650 = "/darwin_indices/darwin17_12"
    storage_folder651 = "/darwin_indices/darwin9_24"
    storage_folder652 = "/darwin_indices/darwin17_15"
    storage_folder653 = "/darwin_indices/darwin14_32"
    storage_folder654 = "/darwin_indices/darwin20_35"
    storage_folder655 = "/darwin_indices/darwin13_25"
    storage_folder656 = "/darwin_indices/darwin1_10"
    storage_folder657 = "/darwin_indices/darwin5_20"
    storage_folder658 = "/darwin_indices/darwin18_36"
    storage_folder659 = "/darwin_indices/darwin6_38"
    storage_folder660 = "/darwin_indices/darwin2_30"
    storage_folder661 = "/darwin_indices/darwin5_27"
    storage_folder662 = "/darwin_indices/darwin1_17"
    storage_folder663 = "/darwin_indices/darwin5_18"
    storage_folder664 = "/darwin_indices/darwin1_28"
    storage_folder665 = "/darwin_indices/darwin18_31"
    storage_folder666 = "/darwin_indices/darwin5_11"
    storage_folder667 = "/darwin_indices/darwin1_21"
    storage_folder668 = "/darwin_indices/darwin6_36"
    storage_folder669 = "/darwin_indices/darwin6_31"
    storage_folder670 = "/darwin_indices/darwin1_26"
    storage_folder671 = "/darwin_indices/darwin5_16"
    storage_folder672 = "/darwin_indices/darwin1_19"
    storage_folder673 = "/darwin_indices/darwin5_29"
    storage_folder674 = "/darwin_indices/darwin8_12"
    storage_folder675 = "/darwin_indices/darwin11_4"
    storage_folder676 = "/darwin_indices/darwin11_34"
    storage_folder677 = "/darwin_indices/darwin13_9"
    storage_folder678 = "/darwin_indices/darwin19_7"
    storage_folder679 = "/darwin_indices/darwin16_23"
    storage_folder680 = "/darwin_indices/darwin8_7"
    storage_folder681 = "/darwin_indices/darwin12_13"
    storage_folder682 = "/darwin_indices/darwin2_9"
    storage_folder683 = "/darwin_indices/darwin4_42"
    storage_folder684 = "/darwin_indices/darwin11_3"
    storage_folder685 = "/darwin_indices/darwin8_15"
    storage_folder686 = "/darwin_indices/darwin4_45"
    storage_folder687 = "/darwin_indices/darwin12_14"
    storage_folder688 = "/darwin_indices/darwin16_24"
    storage_folder689 = "/darwin_indices/darwin11_33"
    storage_folder690 = "/darwin_indices/darwin8_9"
    storage_folder691 = "/darwin_indices/darwin2_7"
    storage_folder692 = "/darwin_indices/darwin8_23"
    storage_folder693 = "/darwin_indices/darwin13_7"
    storage_folder694 = "/darwin_indices/darwin19_9"
    storage_folder695 = "/darwin_indices/darwin15_35"
    storage_folder696 = "/darwin_indices/darwin12_22"
    storage_folder697 = "/darwin_indices/darwin21_32"
    storage_folder698 = "/darwin_indices/darwin8_24"
    storage_folder699 = "/darwin_indices/darwin16_15"
    storage_folder700 = "/darwin_indices/darwin12_25"
    storage_folder701 = "/darwin_indices/darwin21_35"
    storage_folder702 = "/darwin_indices/darwin15_32"
    storage_folder703 = "/darwin_indices/darwin3_37"
    storage_folder704 = "/darwin_indices/darwin4_20"
    storage_folder705 = "/darwin_indices/darwin19_36"
    storage_folder706 = "/darwin_indices/darwin7_38"
    storage_folder707 = "/darwin_indices/darwin4_27"
    storage_folder708 = "/darwin_indices/darwin3_30"
    storage_folder709 = "/darwin_indices/darwin4_5"
    storage_folder710 = "/darwin_indices/darwin4_18"
    storage_folder711 = "/darwin_indices/darwin15_5"
    storage_folder712 = "/darwin_indices/darwin19_31"
    storage_folder713 = "/darwin_indices/darwin4_11"
    storage_folder714 = "/darwin_indices/darwin12_40"
    storage_folder715 = "/darwin_indices/darwin7_36"
    storage_folder716 = "/darwin_indices/darwin3_39"
    storage_folder717 = "/darwin_indices/darwin6_1"
    storage_folder718 = "/darwin_indices/darwin17_1"
    storage_folder719 = "/darwin_indices/darwin7_31"
    storage_folder720 = "/darwin_indices/darwin4_16"
    storage_folder721 = "/darwin_indices/darwin17_6"
    storage_folder722 = "/darwin_indices/darwin4_29"
    storage_folder723 = "/darwin_indices/darwin6_6"
    storage_folder724 = "/darwin_indices/darwin2_1"
    storage_folder725 = "/darwin_indices/darwin13_1"
    storage_folder726 = "/darwin_indices/darwin8_25"
    storage_folder727 = "/darwin_indices/darwin15_33"
    storage_folder728 = "/darwin_indices/darwin12_24"
    storage_folder729 = "/darwin_indices/darwin21_34"
    storage_folder730 = "/darwin_indices/darwin16_14"
    storage_folder731 = "/darwin_indices/darwin8_22"
    storage_folder732 = "/darwin_indices/darwin19_8"
    storage_folder733 = "/darwin_indices/darwin13_6"
    storage_folder734 = "/darwin_indices/darwin2_6"
    storage_folder735 = "/darwin_indices/darwin8_8"
    storage_folder736 = "/darwin_indices/darwin16_13"
    storage_folder737 = "/darwin_indices/darwin12_23"
    storage_folder738 = "/darwin_indices/darwin21_33"
    storage_folder739 = "/darwin_indices/darwin15_34"
    storage_folder740 = "/darwin_indices/darwin11_2"
    storage_folder741 = "/darwin_indices/darwin8_14"
    storage_folder742 = "/darwin_indices/darwin11_32"
    storage_folder743 = "/darwin_indices/darwin19_1"
    storage_folder744 = "/darwin_indices/darwin16_25"
    storage_folder745 = "/darwin_indices/darwin4_44"
    storage_folder746 = "/darwin_indices/darwin8_1"
    storage_folder747 = "/darwin_indices/darwin12_15"
    storage_folder748 = "/darwin_indices/darwin8_13"
    storage_folder749 = "/darwin_indices/darwin11_5"
    storage_folder750 = "/darwin_indices/darwin2_8"
    storage_folder751 = "/darwin_indices/darwin8_6"
    storage_folder752 = "/darwin_indices/darwin12_12"
    storage_folder753 = "/darwin_indices/darwin4_43"
    storage_folder754 = "/darwin_indices/darwin19_6"
    storage_folder755 = "/darwin_indices/darwin16_22"
    storage_folder756 = "/darwin_indices/darwin11_35"
    storage_folder757 = "/darwin_indices/darwin4_17"
    storage_folder758 = "/darwin_indices/darwin7_30"
    storage_folder759 = "/darwin_indices/darwin6_7"
    storage_folder760 = "/darwin_indices/darwin4_28"
    storage_folder761 = "/darwin_indices/darwin17_7"
    storage_folder762 = "/darwin_indices/darwin7_37"
    storage_folder763 = "/darwin_indices/darwin4_10"
    storage_folder764 = "/darwin_indices/darwin12_41"
    storage_folder765 = "/darwin_indices/darwin3_38"
    storage_folder766 = "/darwin_indices/darwin17_9"
    storage_folder767 = "/darwin_indices/darwin3_31"
    storage_folder768 = "/darwin_indices/darwin4_26"
    storage_folder769 = "/darwin_indices/darwin6_9"
    storage_folder770 = "/darwin_indices/darwin15_4"
    storage_folder771 = "/darwin_indices/darwin19_30"
    storage_folder772 = "/darwin_indices/darwin4_19"
    storage_folder773 = "/darwin_indices/darwin4_4"
    storage_folder774 = "/darwin_indices/darwin4_21"
    storage_folder775 = "/darwin_indices/darwin3_36"
    storage_folder776 = "/darwin_indices/darwin4_3"
    storage_folder777 = "/darwin_indices/darwin19_37"
    storage_folder778 = "/darwin_indices/darwin7_39"

    loaded_index = combine_darwin_indices(
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
                                storage_folder26,
                                storage_folder27,
                                storage_folder28,
                                storage_folder29,
                                storage_folder30,
                                storage_folder31,
                                storage_folder32,
                                storage_folder33,
                                storage_folder34,
                                storage_folder35,
                                storage_folder36,
                                storage_folder37,
                                storage_folder38,
                                storage_folder39,
                                storage_folder40,
                                storage_folder41,
                                storage_folder42,
                                storage_folder43,
                                storage_folder44,
                                storage_folder45,
                                storage_folder46,
                                storage_folder47,
                                storage_folder48,
                                storage_folder49,
                                storage_folder50,
                                storage_folder51,
                                storage_folder52,
                                storage_folder53,
                                storage_folder54,
                                storage_folder55,
                                storage_folder56,
                                storage_folder57,
                                storage_folder58,
                                storage_folder59,
                                storage_folder60,
                                storage_folder61,
                                storage_folder62,
                                storage_folder63,
                                storage_folder64,
                                storage_folder65,
                                storage_folder66,
                                storage_folder67,
                                storage_folder68,
                                storage_folder69,
                                storage_folder70,
                                storage_folder71,
                                storage_folder72,
                                storage_folder73,
                                storage_folder74,
                                storage_folder75,
                                storage_folder76,
                                storage_folder77,
                                storage_folder78,
                                storage_folder79,
                                storage_folder80,
                                storage_folder81,
                                storage_folder82,
                                storage_folder83,
                                storage_folder84,
                                storage_folder85,
                                storage_folder86,
                                storage_folder87,
                                storage_folder88,
                                storage_folder89,
                                storage_folder90,
                                storage_folder91,
                                storage_folder92,
                                storage_folder93,
                                storage_folder94,
                                storage_folder95,
                                storage_folder96,
                                storage_folder97,
                                storage_folder98,
                                storage_folder99,
                                storage_folder100,
                                storage_folder101,
                                storage_folder102,
                                storage_folder103,
                                storage_folder104,
                                storage_folder105,
                                storage_folder106,
                                storage_folder107,
                                storage_folder108,
                                storage_folder109,
                                storage_folder110,
                                storage_folder111,
                                storage_folder112,
                                storage_folder113,
                                storage_folder114,
                                storage_folder115,
                                storage_folder116,
                                storage_folder117,
                                storage_folder118,
                                storage_folder119,
                                storage_folder120,
                                storage_folder121,
                                storage_folder122,
                                storage_folder123,
                                storage_folder124,
                                storage_folder125,
                                storage_folder126,
                                storage_folder127,
                                storage_folder128,
                                storage_folder129,
                                storage_folder130,
                                storage_folder131,
                                storage_folder132,
                                storage_folder133,
                                storage_folder134,
                                storage_folder135,
                                storage_folder136,
                                storage_folder137,
                                storage_folder138,
                                storage_folder139,
                                storage_folder140,
                                storage_folder141,
                                storage_folder142,
                                storage_folder143,
                                storage_folder144,
                                storage_folder145,
                                storage_folder146,
                                storage_folder147,
                                storage_folder148,
                                storage_folder149,
                                storage_folder150,
                                storage_folder151,
                                storage_folder152,
                                storage_folder153,
                                storage_folder154,
                                storage_folder155,
                                storage_folder156,
                                storage_folder157,
                                storage_folder158,
                                storage_folder159,
                                storage_folder160,
                                storage_folder161,
                                storage_folder162,
                                storage_folder163,
                                storage_folder164,
                                storage_folder165,
                                storage_folder166,
                                storage_folder167,
                                storage_folder168,
                                storage_folder169,
                                storage_folder170,
                                storage_folder171,
                                storage_folder172,
                                storage_folder173,
                                storage_folder174,
                                storage_folder175,
                                storage_folder176,
                                storage_folder177,
                                storage_folder178,
                                storage_folder179,
                                storage_folder180,
                                storage_folder181,
                                storage_folder182,
                                storage_folder183,
                                storage_folder184,
                                storage_folder185,
                                storage_folder186,
                                storage_folder187,
                                storage_folder188,
                                storage_folder189,
                                storage_folder190,
                                storage_folder191,
                                storage_folder192,
                                storage_folder193,
                                storage_folder194,
                                storage_folder195,
                                storage_folder196,
                                storage_folder197,
                                storage_folder198,
                                storage_folder199,
                                storage_folder200,
                                storage_folder201,
                                storage_folder202,
                                storage_folder203,
                                storage_folder204,
                                storage_folder205,
                                storage_folder206,
                                storage_folder207,
                                storage_folder208,
                                storage_folder209,
                                storage_folder210,
                                storage_folder211,
                                storage_folder212,
                                storage_folder213,
                                storage_folder214,
                                storage_folder215,
                                storage_folder216,
                                storage_folder217,
                                storage_folder218,
                                storage_folder219,
                                storage_folder220,
                                storage_folder221,
                                storage_folder222,
                                storage_folder223,
                                storage_folder224,
                                storage_folder225,
                                storage_folder226,
                                storage_folder227,
                                storage_folder228,
                                storage_folder229,
                                storage_folder230,
                                storage_folder231,
                                storage_folder232,
                                storage_folder233,
                                storage_folder234,
                                storage_folder235,
                                storage_folder236,
                                storage_folder237,
                                storage_folder238,
                                storage_folder239,
                                storage_folder240,
                                storage_folder241,
                                storage_folder242,
                                storage_folder243,
                                storage_folder244,
                                storage_folder245,
                                storage_folder246,
                                storage_folder247,
                                storage_folder248,
                                storage_folder249,
                                storage_folder250,
                                storage_folder251,
                                storage_folder252,
                                storage_folder253,
                                storage_folder254,
                                storage_folder255,
                                storage_folder256,
                                storage_folder257,
                                storage_folder258,
                                storage_folder259,
                                storage_folder260,
                                storage_folder261,
                                storage_folder262,
                                storage_folder263,
                                storage_folder264,
                                storage_folder265,
                                storage_folder266,
                                storage_folder267,
                                storage_folder268,
                                storage_folder269,
                                storage_folder270,
                                storage_folder271,
                                storage_folder272,
                                storage_folder273,
                                storage_folder274,
                                storage_folder275,
                                storage_folder276,
                                storage_folder277,
                                storage_folder278,
                                storage_folder279,
                                storage_folder280,
                                storage_folder281,
                                storage_folder282,
                                storage_folder283,
                                storage_folder284,
                                storage_folder285,
                                storage_folder286,
                                storage_folder287,
                                storage_folder288,
                                storage_folder289,
                                storage_folder290,
                                storage_folder291,
                                storage_folder292,
                                storage_folder293,
                                storage_folder294,
                                storage_folder295,
                                storage_folder296,
                                storage_folder297,
                                storage_folder298,
                                storage_folder299,
                                storage_folder300,
                                storage_folder301,
                                storage_folder302,
                                storage_folder303,
                                storage_folder304,
                                storage_folder305,
                                storage_folder306,
                                storage_folder307,
                                storage_folder308,
                                storage_folder309,
                                storage_folder310,
                                storage_folder311,
                                storage_folder312,
                                storage_folder313,
                                storage_folder314,
                                storage_folder315,
                                storage_folder316,
                                storage_folder317,
                                storage_folder318,
                                storage_folder319,
                                storage_folder320,
                                storage_folder321,
                                storage_folder322,
                                storage_folder323,
                                storage_folder324,
                                storage_folder325,
                                storage_folder326,
                                storage_folder327,
                                storage_folder328,
                                storage_folder329,
                                storage_folder330,
                                storage_folder331,
                                storage_folder332,
                                storage_folder333,
                                storage_folder334,
                                storage_folder335,
                                storage_folder336,
                                storage_folder337,
                                storage_folder338,
                                storage_folder339,
                                storage_folder340,
                                storage_folder341,
                                storage_folder342,
                                storage_folder343,
                                storage_folder344,
                                storage_folder345,
                                storage_folder346,
                                storage_folder347,
                                storage_folder348,
                                storage_folder349,
                                storage_folder350,
                                storage_folder351,
                                storage_folder352,
                                storage_folder353,
                                storage_folder354,
                                storage_folder355,
                                storage_folder356,
                                storage_folder357,
                                storage_folder358,
                                storage_folder359,
                                storage_folder360,
                                storage_folder361,
                                storage_folder362,
                                storage_folder363,
                                storage_folder364,
                                storage_folder365,
                                storage_folder366,
                                storage_folder367,
                                storage_folder368,
                                storage_folder369,
                                storage_folder370,
                                storage_folder371,
                                storage_folder372,
                                storage_folder373,
                                storage_folder374,
                                storage_folder375,
                                storage_folder376,
                                storage_folder377,
                                storage_folder378,
                                storage_folder379,
                                storage_folder380,
                                storage_folder381,
                                storage_folder382,
                                storage_folder383,
                                storage_folder384,
                                storage_folder385,
                                storage_folder386,
                                storage_folder387,
                                storage_folder388,
                                storage_folder389,
                                storage_folder390,
                                storage_folder391,
                                storage_folder392,
                                storage_folder393,
                                storage_folder394,
                                storage_folder395,
                                storage_folder396,
                                storage_folder397,
                                storage_folder398,
                                storage_folder399,
                                storage_folder400,
                                storage_folder401,
                                storage_folder402,
                                storage_folder403,
                                storage_folder404,
                                storage_folder405,
                                storage_folder406,
                                storage_folder407,
                                storage_folder408,
                                storage_folder409,
                                storage_folder410,
                                storage_folder411,
                                storage_folder412,
                                storage_folder413,
                                storage_folder414,
                                storage_folder415,
                                storage_folder416,
                                storage_folder417,
                                storage_folder418,
                                storage_folder419,
                                storage_folder420,
                                storage_folder421,
                                storage_folder422,
                                storage_folder423,
                                storage_folder424,
                                storage_folder425,
                                storage_folder426,
                                storage_folder427,
                                storage_folder428,
                                storage_folder429,
                                storage_folder430,
                                storage_folder431,
                                storage_folder432,
                                storage_folder433,
                                storage_folder434,
                                storage_folder435,
                                storage_folder436,
                                storage_folder437,
                                storage_folder438,
                                storage_folder439,
                                storage_folder440,
                                storage_folder441,
                                storage_folder442,
                                storage_folder443,
                                storage_folder444,
                                storage_folder445,
                                storage_folder446,
                                storage_folder447,
                                storage_folder448,
                                storage_folder449,
                                storage_folder450,
                                storage_folder451,
                                storage_folder452,
                                storage_folder453,
                                storage_folder454,
                                storage_folder455,
                                storage_folder456,
                                storage_folder457,
                                storage_folder458,
                                storage_folder459,
                                storage_folder460,
                                storage_folder461,
                                storage_folder462,
                                storage_folder463,
                                storage_folder464,
                                storage_folder465,
                                storage_folder466,
                                storage_folder467,
                                storage_folder468,
                                storage_folder469,
                                storage_folder470,
                                storage_folder471,
                                storage_folder472,
                                storage_folder473,
                                storage_folder474,
                                storage_folder475,
                                storage_folder476,
                                storage_folder477,
                                storage_folder478,
                                storage_folder479,
                                storage_folder480,
                                storage_folder481,
                                storage_folder482,
                                storage_folder483,
                                storage_folder484,
                                storage_folder485,
                                storage_folder486,
                                storage_folder487,
                                storage_folder488,
                                storage_folder489,
                                storage_folder490,
                                storage_folder491,
                                storage_folder492,
                                storage_folder493,
                                storage_folder494,
                                storage_folder495,
                                storage_folder496,
                                storage_folder497,
                                storage_folder498,
                                storage_folder499,
                                storage_folder500,
                                storage_folder501,
                                storage_folder502,
                                storage_folder503,
                                storage_folder504,
                                storage_folder505,
                                storage_folder506,
                                storage_folder507,
                                storage_folder508,
                                storage_folder509,
                                storage_folder510,
                                storage_folder511,
                                storage_folder512,
                                storage_folder513,
                                storage_folder514,
                                storage_folder515,
                                storage_folder516,
                                storage_folder517,
                                storage_folder518,
                                storage_folder519,
                                storage_folder520,
                                storage_folder521,
                                storage_folder522,
                                storage_folder523,
                                storage_folder524,
                                storage_folder525,
                                storage_folder526,
                                storage_folder527,
                                storage_folder528,
                                storage_folder529,
                                storage_folder530,
                                storage_folder531,
                                storage_folder532,
                                storage_folder533,
                                storage_folder534,
                                storage_folder535,
                                storage_folder536,
                                storage_folder537,
                                storage_folder538,
                                storage_folder539,
                                storage_folder540,
                                storage_folder541,
                                storage_folder542,
                                storage_folder543,
                                storage_folder544,
                                storage_folder545,
                                storage_folder546,
                                storage_folder547,
                                storage_folder548,
                                storage_folder549,
                                storage_folder550,
                                storage_folder551,
                                storage_folder552,
                                storage_folder553,
                                storage_folder554,
                                storage_folder555,
                                storage_folder556,
                                storage_folder557,
                                storage_folder558,
                                storage_folder559,
                                storage_folder560,
                                storage_folder561,
                                storage_folder562,
                                storage_folder563,
                                storage_folder564,
                                storage_folder565,
                                storage_folder566,
                                storage_folder567,
                                storage_folder568,
                                storage_folder569,
                                storage_folder570,
                                storage_folder571,
                                storage_folder572,
                                storage_folder573,
                                storage_folder574,
                                storage_folder575,
                                storage_folder576,
                                storage_folder577,
                                storage_folder578,
                                storage_folder579,
                                storage_folder580,
                                storage_folder581,
                                storage_folder582,
                                storage_folder583,
                                storage_folder584,
                                storage_folder585,
                                storage_folder586,
                                storage_folder587,
                                storage_folder588,
                                storage_folder589,
                                storage_folder590,
                                storage_folder591,
                                storage_folder592,
                                storage_folder593,
                                storage_folder594,
                                storage_folder595,
                                storage_folder596,
                                storage_folder597,
                                storage_folder598,
                                storage_folder599,
                                storage_folder600,
                                storage_folder601,
                                storage_folder602,
                                storage_folder603,
                                storage_folder604,
                                storage_folder605,
                                storage_folder606,
                                storage_folder607,
                                storage_folder608,
                                storage_folder609,
                                storage_folder610,
                                storage_folder611,
                                storage_folder612,
                                storage_folder613,
                                storage_folder614,
                                storage_folder615,
                                storage_folder616,
                                storage_folder617,
                                storage_folder618,
                                storage_folder619,
                                storage_folder620,
                                storage_folder621,
                                storage_folder622,
                                storage_folder623,
                                storage_folder624,
                                storage_folder625,
                                storage_folder626,
                                storage_folder627,
                                storage_folder628,
                                storage_folder629,
                                storage_folder630,
                                storage_folder631,
                                storage_folder632,
                                storage_folder633,
                                storage_folder634,
                                storage_folder635,
                                storage_folder636,
                                storage_folder637,
                                storage_folder638,
                                storage_folder639,
                                storage_folder640,
                                storage_folder641,
                                storage_folder642,
                                storage_folder643,
                                storage_folder644,
                                storage_folder645,
                                storage_folder646,
                                storage_folder647,
                                storage_folder648,
                                storage_folder649,
                                storage_folder650,
                                storage_folder651,
                                storage_folder652,
                                storage_folder653,
                                storage_folder654,
                                storage_folder655,
                                storage_folder656,
                                storage_folder657,
                                storage_folder658,
                                storage_folder659,
                                storage_folder660,
                                storage_folder661,
                                storage_folder662,
                                storage_folder663,
                                storage_folder664,
                                storage_folder665,
                                storage_folder666,
                                storage_folder667,
                                storage_folder668,
                                storage_folder669,
                                storage_folder670,
                                storage_folder671,
                                storage_folder672,
                                storage_folder673,
                                storage_folder674,
                                storage_folder675,
                                storage_folder676,
                                storage_folder677,
                                storage_folder678,
                                storage_folder679,
                                storage_folder680,
                                storage_folder681,
                                storage_folder682,
                                storage_folder683,
                                storage_folder684,
                                storage_folder685,
                                storage_folder686,
                                storage_folder687,
                                storage_folder688,
                                storage_folder689,
                                storage_folder690,
                                storage_folder691,
                                storage_folder692,
                                storage_folder693,
                                storage_folder694,
                                storage_folder695,
                                storage_folder696,
                                storage_folder697,
                                storage_folder698,
                                storage_folder699,
                                storage_folder700,
                                storage_folder701,
                                storage_folder702,
                                storage_folder703,
                                storage_folder704,
                                storage_folder705,
                                storage_folder706,
                                storage_folder707,
                                storage_folder708,
                                storage_folder709,
                                storage_folder710,
                                storage_folder711,
                                storage_folder712,
                                storage_folder713,
                                storage_folder714,
                                storage_folder715,
                                storage_folder716,
                                storage_folder717,
                                storage_folder718,
                                storage_folder719,
                                storage_folder720,
                                storage_folder721,
                                storage_folder722,
                                storage_folder723,
                                storage_folder724,
                                storage_folder725,
                                storage_folder726,
                                storage_folder727,
                                storage_folder728,
                                storage_folder729,
                                storage_folder730,
                                storage_folder731,
                                storage_folder732,
                                storage_folder733,
                                storage_folder734,
                                storage_folder735,
                                storage_folder736,
                                storage_folder737,
                                storage_folder738,
                                storage_folder739,
                                storage_folder740,
                                storage_folder741,
                                storage_folder742,
                                storage_folder743,
                                storage_folder744,
                                storage_folder745,
                                storage_folder746,
                                storage_folder747,
                                storage_folder748,
                                storage_folder749,
                                storage_folder750,
                                storage_folder751,
                                storage_folder752,
                                storage_folder753,
                                storage_folder754,
                                storage_folder755,
                                storage_folder756,
                                storage_folder757,
                                storage_folder758,
                                storage_folder759,
                                storage_folder760,
                                storage_folder761,
                                storage_folder762,
                                storage_folder763,
                                storage_folder764,
                                storage_folder765,
                                storage_folder766,
                                storage_folder767,
                                storage_folder768,
                                storage_folder769,
                                storage_folder770,
                                storage_folder771,
                                storage_folder772,
                                storage_folder773,
                                storage_folder774,
                                storage_folder775,
                                storage_folder776,
                                storage_folder777,
                                storage_folder778
                            )

    return loaded_index

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

@app.route('/')
@mobile_template('{mobile/}darwin_loading.html')
def darwin_query(template):
    user_logged_in = check_login_state(session)
    
    if user_logged_in:
        return render_template(template)
    
    else:
        return redirect('/login')
    
@app.route('/load_darwin_index')
def old_darwin_load():
    return "Finished!"

@app.route('/darwin', methods=['GET', 'POST'])
@mobile_template('{mobile/}index.html')
def index(template):

    user_logged_in = check_login_state(session)
    
    if user_logged_in:
        loaded_index = load_darwin_resources()

        query_text = None
        query_response = ''

        q_form = QueryForm()

        if q_form.validate_on_submit():
            query_text = q_form.query_string.data

            if loaded_index: # Filter out bad index loads (which will return 'None')
                query_prompt = f"The 'user query' is '{query_text}'."+\
                                " Please only respond to the 'user query' with related information" +\
                                " found only in the provided query_engine object.  If related information" +\
                                " is not found within those 'chunks' then respond with" +\
                                " 'not found'."
                query_engine = loaded_index.as_query_engine()
                query_response = query_engine.query(query_prompt)

        return render_template(template, form=q_form, query_response=query_response)
    
    else:
        return redirect('/login')

@app.route('/pangolin')
@mobile_template('{mobile/}loading.html')
def pangolin_query(template):
    user_logged_in = check_login_state(session)
    
    if user_logged_in:
        return render_template(template)
    
    else:
        return redirect('/login')

@app.route('/load_pangolin_index')
def old_load():
    return "Finished!"

@app.route('/pangolin_loaded', methods=['GET', 'POST'])
@mobile_template('{mobile/}pangolin.html')
def load_pangolin_index(template):
    user_logged_in = check_login_state(session)
    
    if user_logged_in:
    
        p_index = load_pangolin_resources()
        query_text = None
        query_response = ''

        q_form = QueryForm()

        if q_form.validate_on_submit():
            query_text = q_form.query_string.data

            if p_index: # Filter out bad index loads (which will return 'None')
                print("Index exists!")
                query_engine = p_index.as_query_engine()
                
                query_prompt = f"The 'user query' is '{query_text}'."+\
                                " Please only respond to the 'user query' with information" +\
                                " found only in the provided 'chunks', 'chunk1' to 'chunk26'.  If the information" +\
                                " is not found within those 'chunks' then respond with" +\
                                " 'not found'."
                
                query_response = query_engine.query(query_prompt)

        return render_template(template, form=q_form, query_response=query_response)
    
    else:
        return redirect('/login')

@app.route('/darwin_site_preview.png')
def prep_mobile_image():
    preview_image_url = "./static/images/social_preview_square.png"
    return send_file(preview_image_url, mimetype='image/png')