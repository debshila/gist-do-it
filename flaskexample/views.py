"""
Created on Mon Jan 28 16:24:35 2019

@author: dbm
"""
#import pyLDAvis
from flaskexample import app

#import topic_model_utils
#import preproc_utils
import pandas as pd
import numpy as np
import nltk
import spacy
nltk.download('punkt')
from flask import Flask, request, render_template, jsonify
from gensim.summarization import summarize, keywords
import gensim as gs
from gensim.test.utils import datapath
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess
from gensim.corpora.dictionary import Dictionary
from nltk.stem import WordNetLemmatizer 
from nltk import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import requests
import validators
import re
from gensim.models import CoherenceModel, LdaModel

# Init the Wordnet Lemmatizer
wnl = WordNetLemmatizer()
#lda_file = datapath("optimal_LDA_model_acl_train_16top_fulldoc_updated")
#lda = LdaModel.load(lda_file)

@app.route('/')
@app.route('/index')
def index():
  product = {'name': 'Gist do it!'}  
  return render_template("index.html", title = 'Home', user = product)

@app.route('/', methods=["POST"])
def get_text():
    text = request.get_json(force=True)['text']
    filt_len = 6
    return_ratio = 0.05
    if validators.url(text):
        r  = requests.get(text)#'https://machinebox.io/privacy'https://www.manulife.com/en/privacy-policy/privacy-statement.html
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')    
        text_1 = soup.findAll(text=True)
    else:
        text_1 = text
    #Preprocess text
    tmp = sent_tokenize(''.join(text_1))
    word_count_orig = len(simple_preprocess(' '.join(tmp)))
    pat = '[^a-zA-z0-9.?! ]+'
    #Keep only sentences
    tmp_sent = [re.sub(pat, '', i).rstrip() for i in tmp]
    tmp_sent = [
        re.sub(pattern='[ \t]{2,}', repl=' ', string=i) for i in tmp_sent
        if len(i) > filt_len
    ]
    # Join cleaned sentences together
    txt = ' '.join(tmp_sent)
    
    # Summarize text
    result = summarize(txt, ratio = return_ratio, split = True)
    title = summarize(txt, word_count = 10, split = True) #
    # Updating pretrained LDA model with new documents
#    new_doc = tokenize(pd.Series(txt), stop_words=stop_words, frequent_words=frequent_words)
#    new_doc= sum(new_doc,[])
#    new_doc_bow = id2word.doc2bow(new_doc)
#    new_doc_top_prob_dist = optimal_model[new_doc_bow]
#    # Sort topic probability distribution for new document
#    new_doc_top_prob_dist_df = pd.DataFrame([{'topic': i[0],'prob': i[1]} for i in new_doc_top_prob_dist]).sort_values(
#    by=['prob'], ascending=False)
#
#    lda.update(other_corpus)
    # count words
    word_count_summary =  len(simple_preprocess(' '.join(result)))

    return jsonify({'Title':title, 'Gist': result, 
                    'orig_wc':word_count_orig, 'summary_wc':word_count_summary})

@app.route('/topics')
def show_lda():
    return render_template('acl_optimal_lda_16top_fulldoc_tsne.html')
