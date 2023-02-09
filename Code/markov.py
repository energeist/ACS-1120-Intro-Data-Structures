from __future__ import division, print_function  # Python 2 and 3 compatibility
from dictogram import Dictogram
from listogram import Listogram
import re
import random

# class Dictogram(dict):
#     """Dictogram is a histogram implemented as a subclass of the dict type."""

#     def __init__(self, word_list=None):
#         """Initialize this histogram as a new dict and count given words."""
#         super(Dictogram, self).__init__()  # Initialize this as a new dict
#         # Add properties to track useful word counts for this histogram
#         self.types = 0  # Count of distinct word types in this histogram
#         self.tokens = 0  # Total count of all word tokens in this histogram
#         # Count words in given list, if any
#         if word_list is not None:
#             for i in range(len(word_list)):
#                 self.add_count(i, word_list[i])

#     # def add_count(self, word, count=1):
#     #     """Increase frequency count of given word by given count amount."""
#     #     # TODO: Increase word frequency by count
        
#     #     if word in self:
#     #         self[word] += count
#     #     else:
#     #         self.update({word: count})
#     #         self.types += 1
#     #     self.tokens += count

#     def frequency(self, word):
#         """Return frequency count of given word, or 0 if word is not found."""
#         # TODO: Retrieve word frequency count
#         return self[word] if self.get(word) else 0

    # def sample(self):
    #     """Return a word from this histogram, randomly sampled by weighting
    #     each word's probability of being chosen by its observed frequency."""
    #     # TODO: Randomly choose a word based on its frequency in this histogram
    #     return random.choices(list(self.keys()), weights = self.values(), k = 1)[0]

#     def markoverize(text):
#         pass


class MarkovChain(dict):
    """MarkovChain creates a Markov chain from a corpus"""
    def __init__(self, word_list = None, dict = None):
        # self.types = 0
        # self.tokens = 0
        super(MarkovChain, self).__init__()
        if word_list is not None:
            for i in range(len(word_list)-1):
                self.add_count(i, word_list)
            self.pop("END")

    def add_count(self, index, word_list, count = 1):
        """Generates a markov histogram from a provided word list"""
        word = word_list[index]
        if word in self:
            self[word].append(word_list[index + 1])
        else:
            self.update({word_list[index]: [word_list[index + 1]]})
        # print(self)

    def random_markov_sentence(self, max_num):
        chosen_words = [random.choice(self["START"])]
        for _ in range(max_num - 1):
            word = random.choice(self[chosen_words[-1]])
            if word == "END":
                break
            chosen_words.append(word)
        sentence = " ".join(chosen_words)
        return sentence


# sentence = "One fish, two fish, red fish, blue fish."
sentence = "One fish, two fish, red fish, blue fish. Fun fish, brew fish, sled fish, shoo fish? Bun fish, shoe fish, dread fish, new fish!"

def add_entry_and_exit(text):
    text = "START " + text
    text = re.sub(r'[,]+', "", text)
    text = re.sub(r'[.!?]+', " END START ", text).split()
    return text



        
markov = MarkovChain(add_entry_and_exit(sentence))
print(markov.random_markov_sentence(10))