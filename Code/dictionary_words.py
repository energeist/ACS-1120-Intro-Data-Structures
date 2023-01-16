import sys
import random
from decorators import runtime_calc

@runtime_calc
def random_sentence():
    num_words = int(sys.argv[1])

    infile = open("/usr/share/dict/words", 'r')
    text = infile.readlines()
    infile.close()
    words = []

    for line in text:
        word = line.strip("\n")
        words.append(word)

    sentence = ""

    for _ in range(num_words):
        random_word = random.choice(words)
        while "'" in random_word:
            random_word = random.choice(words)
        sentence += random_word
        random_word = ""
        if _ < num_words - 1:
            sentence += " "
    sentence += "."
    print(sentence)
    return sentence

if __name__ == "__main__":
    random_sentence()