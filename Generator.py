import collections
import random


class Generator:
    letter_dictionary = collections.defaultdict(list)

    def __init__(self, word_file):
        self.letter_dictionary = collections.defaultdict(list)

        words = open(word_file, 'r')
        for word in words:
            for i in xrange(0, len(word) - 2):
                self.letter_dictionary[word[i] + word[i + 1]].append(word[i + 2])
            self.letter_dictionary[word[-2] + word[-1]].append('\n')

    def generate(self):
        word = random.choice(self.letter_dictionary.keys())

        while word[-1] != '\n':
            word += random.choice(self.letter_dictionary[word[-2] + word[-1]])

        return word
