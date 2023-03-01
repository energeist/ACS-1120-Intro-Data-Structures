"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
from markov import read_source
from markov import markov
from sample import choices_sentence
import sys
import re

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

word_list = read_source(f'./data/volcanoes.txt')

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # num = int(request.args.get('num'))
    sentence = ""
    while len(sentence) < 5:
        sentence = markov.random_markov_sentence(30)
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)