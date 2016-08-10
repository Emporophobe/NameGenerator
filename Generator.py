import collections
import random


class Generator:
    letter_dictionary = collections.defaultdict(list)
    order = 0

    def __init__(self, word_file, order=2):
        self.letter_dictionary = collections.defaultdict(list)
        self.order = order

        words = open(word_file, 'r')
        for word in words:
            for i in xrange(0, len(word) - order):
                self.letter_dictionary[word[i:i + order]].append(word[i + order])
            self.letter_dictionary[word[-order:]].append('\n')

    def generate(self):
        word = random.choice(self.letter_dictionary.keys())

        while word[-1] != '\n':
            word += random.choice(self.letter_dictionary[word[-self.order:]])

        return word[:-1]  # word always ends in a newline
