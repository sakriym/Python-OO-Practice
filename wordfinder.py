class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path_file):
        #call another function
        self.words = self.read_file(path_file)

    def read_file(self,path_file):
        num_word = 0
        with open (path_file, "r") as file:
            for line in file:
                words = line.split()
                num_word += len(words)
                print(num_word)
                return words

    def random(self):
        return random.choice(self.words)