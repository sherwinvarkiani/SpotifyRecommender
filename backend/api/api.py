from flask import Flask, session,make_response,render_template, redirect, request
from flask_cors import CORS, cross_origin
from urllib import parse
import config
import os
import requests
import json
import random

app = Flask(__name__)
CORS(app)

def generateRandomString ():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(chars) for x in range(16))

app.secret_key = generateRandomString();

stateKey = 'spotify_auth_state';

@app.route('/')
def hello_word ():
    return 'App Loaded. This is backend.'

@app.route('/getUserInfo')
def call():
    res = make_response ("AppLoaded")
    res.set_cookie('userID', '1')
    print (app.secret_key,flush=True)
    params={
        'client_id':config.ID,
        'response_type':'code',
        'redirect_uri':config.REDIRECTURI,
        'state': app.secret_key,
        'allow_redirects':True,
    }
    print (config.REDIRECTURI, flush=True)
    session [stateKey] = app.secret_key
    r = requests.get('https://accounts.spotify.com/authorize', params=params)
    r = redirect(r.url, code=302)
    return r


@app.route('/callback')
def resposne_spotify ():
    #Get the code from the query string
    print (session[stateKey], flush=True)
    storedState = session [stateKey] if session else None;
    code = request.args.get('code')
    state = request.args.get('state')

    if (code == None):
        return ("GG")
    if (state == None or state != storedState):
        return ("GG")
    else:
        return ("HERE")
        params = {
            'grant_type': "authorization_code",
            'code':code,
            'redirect_uri':config.REDIRECTURI,
            'client_id':config.ID,
            'client_secret' : config.SECRET
        }
        r = requests.post ('https://accounts.spotify.com/api/token')
