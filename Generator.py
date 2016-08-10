import collections
import random


class Generator:
    letter_dictionary = collections.defaultdict(list)
    order = 0

    # indicates the beginning of a word
    # this lets the beginnings of generated words resemble actual word beginnings
    # instead of looking like they begin in the middle
    word_begin = '^'

    def __init__(self, word_file, order=2):
        self.letter_dictionary = collections.defaultdict(list)
        self.order = order

        with open(word_file, 'r') as words:
            for word in words:
                word = self.word_begin + word  # prepend throwaway character to indicate beginning of word
                for i in xrange(0, len(word) - order):
                    self.letter_dictionary[word[i:i + order]].append(word[i + order])
                self.letter_dictionary[word[-order:]].append('\n')

    def generate(self):
        # start with a sequence which began a word in the corpus
        word = random.choice(filter(lambda x: x[0] == self.word_begin, self.letter_dictionary.keys()))

        while word[-1] != '\n':
            word += random.choice(self.letter_dictionary[word[-self.order:]])

        return word[1:-1]  # word always starts with a throwaway char and ends in a newline
