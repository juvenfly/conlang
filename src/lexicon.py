
class Lexicon(object):
    def __init__(self, phonology, word_list):
        self.phonology = phonology
        self.word_list = set()

    def generate_lexicon(self):
        raise NotImplementedError


class Word(object):
    def __init__(self):
        self.underlying_representation = None
