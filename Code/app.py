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

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # num = int(request.args.get('num'))

    sentence = ""
    order = 2
    min_length = 15

    ## This works
    # while len(sentence) < 5:
    #     markov_chain = ngram(word_list, order)
    #     sentence = generate_markov_sentence(markov_chain, min_length, order)
    # print(markov_chain)
    
    ##This needs work?
    # print(word_list)
    sentence_starters, full_ngram = sentence_ngram(word_list, order)
    print(sentence_starters)
    # print(full_ngram)
    # print(len(word_list))
    # print(full_ngram)
    # generated_text = generate_sentence(chain, 20, order)
    # print(generated_text)
    sentence = generate_sentence_2(full_ngram, sentence_starters, min_length, order)
    return render_template('index.html', sentence=sentence)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
