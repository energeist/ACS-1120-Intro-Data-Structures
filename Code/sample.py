from histogram import histogram
from histogram import read_source
import sys
import timeit
import random

test_text = 'one fish, two fish, red fish, blue fish'
source_text = sys.argv[1]

def random_histogram_word(histogram):
    keys = histogram.keys()
    return list(keys)[random.randint(0,len(keys)-1)]

if __name__ == "__main__":
    word_list = read_source(source_text)
    histogram_output = histogram(word_list)
    print(random_histogram_word(histogram_output))
    pass