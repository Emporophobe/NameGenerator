import Generator


def main():
    g = Generator.Generator("words_en.txt", 3)

    for i in xrange(50):
        print g.generate()


if __name__ == "__main__":
    main()
