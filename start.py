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

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)