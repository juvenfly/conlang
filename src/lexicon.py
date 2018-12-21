from random import sample, randint

from src.phonology import Syllable


class Lexicon(object):
    def __init__(self, phonology, word_list=None):
        self.phonology = phonology
        if word_list:
            self.word_list = word_list
        else:
            self.word_list = []

    def generate_lexicon(self, size=100):
        word_list = []

        i = 0
        while i < size:
            new_word = self.generate_word()
            if new_word.surface_representation not in word_list:
                i += 1
                word_list.append(new_word.surface_representation)

        self.word_list = word_list

    def generate_word(self):
        syllable_count = randint(1, 5)
        syllables = []

        for i in range(syllable_count):
            syllables.append(self.generate_syllable())

        word = Word(syllables)

        return word

    def generate_syllable(self):
        syllable_structure = self.pick_syllable_structure()
        phonemes = self.fill_syllable_structure(syllable_structure)
        syllable = Syllable(phonemes)

        return syllable

    def pick_syllable_structure(self):
        return sample(self.phonology.valid_syllables, 1)[0]

    def fill_syllable_structure(self, syllable_structure):
        """
        Fills out syllables with random consonants & vowels.
        :param syllable_structure: [("C", "V"), ("V", ) ... ] The syllable structure of the word as a list of tuples.
        :return: syllables as a set of phonemes
        """
        syllable = []

        for phoneme_type in syllable_structure:
            phoneme = self.get_random_phoneme(phoneme_type)
            syllable.append(phoneme)

        return syllable

    def get_random_phoneme(self, phoneme_type):
        """
        Gets a random phoneme from phonology of type C or V
        :param phoneme_type: C or V
        :return:
        """
        if phoneme_type not in ['C', 'V']:
            raise ValueError(f'phoneme_type must be "C" or "V", got {phoneme_type} instead')

        type_match = False
        while not type_match:
            phoneme = sample(self.phonology.phonemes, 1)[0]
            if phoneme.type == phoneme_type:
                type_match = True

        return phoneme


class Word(object):
    def __init__(self, syllables):
        self.syllables = syllables
        self.underlying_representation = self._get_underlying_representation()
        self.surface_representation = ''.join(self._get_surface_representation())

    def _get_surface_representation(self):
        surface_representation = []
        for syllable in self.syllables:
            for phoneme in syllable.phonemes:
                surface_representation += phoneme.symbol

        return surface_representation

    def _get_underlying_representation(self):
        underlying_representation = []
        for syllable in self.syllables:
            underlying_representation += syllable.phonemes

        return tuple(underlying_representation)
