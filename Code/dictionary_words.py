import timeit
import sys
import random
# import mmap
from decorators import runtime_calc

num_words = int(sys.argv[1])
words = []

def read_dictionary():
    start = timeit.default_timer()
    with open("/usr/share/dict/words") as text:
        words = text.read().split()
    end = timeit.default_timer()
    print(f'Time to read words: {(end - start):.6f} seconds')  
    return words

# def read_dictionary():
#     start = timeit.default_timer()
#     with open("/usr/share/dict/words", 'rb') as f:
#         mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#         words = mmapped_file.read().decode().split('\n')
#     end = timeit.default_timer()
#     print(f'Time to read words: {end - start} seconds')  
#     return words

@runtime_calc
def random_sentence():
    words = read_dictionary()
    sentence = ""
    chosen_words = []
    for _ in range(num_words):
        random_word = random.choice(words)
        chosen_words.append(random_word)    
    return print(f'{" ".join(chosen_words)}.')

@runtime_calc
def random_sentence_2():
    words = read_dictionary()
    sentence = ""
    index_list = []
    chosen_words = []

    for _ in range(num_words):
        index_list.append(random.randint(0,len(words)-1))
    index_list.sort()

    for index in index_list:
        chosen_words.append(words[index])
    return print(f'{" ".join(chosen_words)}.')

@runtime_calc
def random_sentence_3():
    words = read_dictionary()
    random_words = random.sample(words, k=num_words)
    return print(f"{' '.join(random_words)}.")

if __name__ == "__main__":

    random_sentence()
    random_sentence_2()
    random_sentence_3()
