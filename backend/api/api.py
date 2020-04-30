from flask import Flask, make_response,render_template, redirect
from flask_cors import CORS, cross_origin

import config

import requests
import json


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_word ():
    return 'App Loaded. This is backend.'

@app.route('/getUserInfo')
def call():
    res = make_response ("AppLoaded")
    res.set_cookie('userID', '1')
    params={
        'client_id':config.ID,
        'response_type':'code',
        'redirect_uri':config.REDIRECTURI,
        'state': config.ID + "~" + config.SECRET,
        'allow_redirects':True,
    }
    r = requests.get('https://accounts.spotify.com/authorize', params=params)
    print(config.REDIRECTURI,flush=True)
    r = redirect(r.url, code=302)
    return r


@app.route('/callback')
def resposne_spotify ():
    print ("here")
    return "here"