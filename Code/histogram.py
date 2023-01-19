import sys
import timeit
import re

test_text = 'one fish, two fish, red fish, blue fish'

source_text = sys.argv[1]

# add items by key and increment
def histogram(source_text):
    histogram = {}
    with open(f"./{source_text}") as text:
        words = re.split(r'\W+',text.read())
    for word in words:
        word = word.lower()
        if word in histogram:
            histogram[word.lower()] += 1
        else:
            histogram[word.lower()] = 1
    return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))

# add items by count of list (slow)
def histogram2(source_text):
    histogram = {}
    with open(f"./{source_text}") as text:
        words = re.split(r'\W+',text.read())
    for word in words:
        word = word.lower()
        histogram[word] = words.count(word)
    return dict(sorted(histogram.items(), key=lambda x: x[1], reverse=True))

def invert(histogram_to_invert):
    inverted_histogram = {}
    for key in histogram_to_invert.keys():
        
        if histogram_to_invert[key] in inverted_histogram:
            inverted_histogram[histogram_to_invert[key]].append(key)
        else:
            inverted_histogram[histogram_to_invert[key]] = [key]
    return(inverted_histogram) 

def unique_words(histogram):
    return len(histogram.keys())

def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    start = timeit.default_timer()
    print(histogram(source_text))
    print(unique_words(histogram2(source_text)))
    print(frequency(sys.argv[2], histogram2(source_text)))
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")
    # start = timeit.default_timer()
    # print(histogram2(source_text))
    # print(unique_words(histogram2(source_text)))
    # print(frequency(sys.argv[2], histogram2(source_text)))
    # end = timeit.default_timer()
    # print(f"Time to run {end - start} seconds\n")
    start = timeit.default_timer()
    print(invert(histogram(source_text)))
    end = timeit.default_timer()
    print(f"Time to run {end - start} seconds\n")