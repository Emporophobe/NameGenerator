import sys

import Generator


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print "Usage: python " + sys.argv[0] + " input_file words_to_generate [markov_chain_order=2]"
        print "Example: python " + sys.argv[0] + " words.txt 10"
        sys.exit(1)

    order = int(sys.argv[3]) if len(sys.argv) == 4 else 2

    g = Generator.Generator(sys.argv[1], order)

    for i in xrange(int(sys.argv[2])):
        print g.generate()


if __name__ == "__main__":
    main()
