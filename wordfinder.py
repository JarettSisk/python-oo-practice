"""Word Finder: finds random words from a dictionary."""
# needed in order to get random values from list.
import random

# WordFinder class
class WordFinder:
    """Class that reads / stores a list of words from a file, then allows you to get back a random word.
    Takes one paramater (file_path) => a path to a txt file containing words. Example: wf = WordFinder("my-words.txt")
    >>> wf = WordFinder("words.txt")

    >>> isinstance(wf.random(), str)
    True
    """
    def __init__(self, file_path):
        self.words_list = self.get_words_list(file_path)


    def random(self):
        """ Prints random word from list"""
        return random.choice(self.words_list)

    # Get list of words from file
    def get_words_list(self, file_path):
        words = []
        words_file = open(file_path, "r")
        for line in words_file:
                for word in line.split():
                    words.append(word)

        return words


# Intantiate new WordFinder
wf = WordFinder("words.txt")

# Print random word
wf.random()


class SpecialWordFinder(WordFinder):
    """A subclass of the WordFinder class that prints random words, excluding blank lines or comments.
    Takes one paramater (file_path) => a path to a txt file containing words. Example: swf = SpecialWordFinder("my-words.txt")
    """
    def __init__(self, file_path):
        self.words_list = self.get_special_words_list(file_path)

    def get_special_words_list(self, file_path):
        "Prints random word from list, exluding any comment lines of blank lines"
        words = []
        words_file = open(file_path, "r")
        for line in words_file:
            if line[0] != "#":
                for word in line.split():
                    if word != "":
                        words.append(word)

        return words

# Intantiate new SpecialWordFinder
swf = SpecialWordFinder("special-words.txt")

# Print random word
swf.random()

