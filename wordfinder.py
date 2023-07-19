import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_file):
        # call another function
        self.words = self.read_file(path_file)

    def read_file(self, path_file):
        # num_word = 0
        # open the file in this path as file(variable name - file object
        # we can iterate over)
        with open(path_file, "r") as file:
            # for line in file:
            #     #TODO: only equal to one line of words by placing words in for
            #     words = line.split()
            #     num_word += len(words)
            #     print(num_word)
            #     # TODO: short-circuit by returning after one line
            #     return words

            # returns a list of each line in file
            return [line.strip() for line in file]

    def random(self):
        return random.choice(self.words)

# TODO: Idea of polymorphism.
    # Lean on the functionality of the parent method read file
    # use the function to make changes then do following changes


class SpecialWordFind(WordFinder):
    # constructor function contains super keyword to leverage parent functions
    def __init__(self, path_file):
        # TODO: call the parent dunder init and pass in the path file
        super().__init__(path_file)

    # When you define a method in a class, first argument MUST BE self

    def read_file(self, path_file):
        # create a function to remove the hash and spaces
        # to overwrite the parent read file, name the child function as the
        # same name but implement what we want different in this function
        # TODO: Need to open the file first
        # for line in path_file:
        #     line = line.strip()

        #     if line.startswith('#'):
        #         continue

        #     else:
        #         print(line)

        # we are calling the parent read file with super keyword
        # a list of every line in the file
        words = super().read_file(path_file)

        # only put words in my new list if they are not an empty string
        # and do not start with a #
        return [w for w in words if w != '' and not w.startswith('#')]
