from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-character-standard')
def create_character_standard():
    return render_template('character-creator-standard.html')

@app.route('/create-character-homebrew')
def create_character_homebrew():
    return render_template('character-creator-homebrew.html')
