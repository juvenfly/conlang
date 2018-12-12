
class Lexicon(object):
    def __init__(self, phonology, word_list):
        self.phonology = phonology
        self.word_list = set()

    def generate_lexicon(self):
        raise NotImplementedError


class Word(object):
    def __init__(self, syllables):
        self.syllables = syllables
        self.underlying_representation = self._get_underlying_representation()

    def _get_underlying_representation(self):
        underlying_representation = []
        for syllable in self.syllables:
            underlying_representation += syllable.phonemes

        return tuple(underlying_representation)

    def get_word(self):
        result = []
        for phoneme in self.underlying_representation:
            result += phoneme.symbol

        return ''.join(result)
