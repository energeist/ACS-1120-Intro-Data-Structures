"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
from higher_order_markov import ngram, generate_markov_sentence, sentence_ngram, generate_sentence_2
from markov import read_source_2
from markov import markov
from sample import choices_sentence
import sys
import re

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

word_list = read_source_2(f'./data/marx.txt')
# print(word_list)
markov_chain = {}
# Initialize with 2nd order markov chain
order = 2
sentence_starters, full_ngram = sentence_ngram(word_list, order)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = ""
    # if order != 2:
    #     sentence_starters, full_ngram = sentence_ngram(word_list, order)
    # print(sentence_starters)
    generated_text = '' 
    num_sentences = int(request.args.get('num_sentences'))
    # num_sentences = 2
    for _ in range(num_sentences):
        sentence = generate_sentence_2(full_ngram, sentence_starters, order)
        generated_text += sentence + " "
    return render_template('index.html', sentence=generated_text)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
