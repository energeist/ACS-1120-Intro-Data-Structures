import sys
import timeit
import re

test_text = 'one fish, two fish, red fish, blue fish'

source_text = sys.argv[1]

def histogram(source_text):
    histogram = {}
    with open(f"./{source_text}") as text:
        words = text.read().split()
    for word in words:
        word = re.sub(r'\W+', '', word)
        if word in histogram:
            histogram[word.lower()] += 1
        else:
            histogram[word.lower()] = 1
    return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))

def unique_words(histogram):
    return len(histogram.keys())


def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    print(histogram(source_text))
    print(unique_words(histogram(source_text)))
    print(frequency(sys.argv[2], histogram(source_text)))