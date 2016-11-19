from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def start():
    return index.html

@app.route('/stats')
def health():
	os.system('findandaddsubnets.py')

@app.route('/addsubnets')
def add():
	os.system('findandaddsubnets.py')

