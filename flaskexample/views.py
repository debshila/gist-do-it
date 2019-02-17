"""
Created on Mon Jan 28 16:24:35 2019

@author: dbm
"""
#import pyLDAvis
import os
from flaskexample import app
from flask import Flask, request, render_template, jsonify
from gensim.summarization import summarize, keywords
import gensim as gs
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer 
from nltk import sent_tokenize
# Init the Wordnet Lemmatizer
wnl = WordNetLemmatizer()


@app.route('/')
@app.route('/index')
def index():
  product = {'name': 'Gist do it!'}  
  return render_template("index2.html", title = 'Home', user = product)

@app.route('/', methods=["POST"])
def get_text():
    text = request.get_json(force=True)['text']
    result = summarize(text, ratio = 0.20, split = True)
    title = summarize(text, ratio = 0.08, split = True) #

    return jsonify({'Title':title, 'Gist': result})

@app.route('/topics')
def show_lda():
    return render_template('acl_optimal_lda_35.html')
