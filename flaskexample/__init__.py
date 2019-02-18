#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:39:24 2019

@author: dbm
"""
from flask import Flask
import logging
import sys

app = Flask(__name__, template_folder='template')
from flaskexample import views

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)