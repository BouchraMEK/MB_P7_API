#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from flask import Flask, jsonify
import joblib

app = Flask(__name__)


#Premiers pas sur l'API
@app.route('/')
def index():
    return 'Welcome to my Flask API for prediction of loan giving '



# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)
    #app.run('localhost', 5000)


