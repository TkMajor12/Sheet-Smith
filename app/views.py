from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-character')
def create_character():
    return render_template('character-creator.html')
