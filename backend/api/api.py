from flask import Flask
import config

import requests
import json


app = Flask(__name__)

@app.route('/')
def hello_word():
    print (config.ID)
    params={
        'client_id':''
    }
    return 'Hello, World'

