from random import sample, randint

from src.phonology import Consonant, Vowel, Syllable


class Lexicon(object):
    def __init__(self, phonology, word_list=None):
        self.phonology = phonology
        if word_list:
            self.word_list = word_list
        else:
            self.word_list = set()

    def generate_lexicon(self):
        word_list = set()

        for i in range(100):
            new_word = self.generate_word()
            print(f'NEW WORD: {new_word.surface_representation}')
            if new_word in word_list:
                i -= 1
            word_list.add(new_word)

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
        return sample(self.phonology.valid_syllables, 1)

    def fill_syllable_structure(self, syllable_structure):
        syllable = set()

        for i, phoneme_type in enumerate(syllable_structure):
            phoneme = self.get_random_phoneme(phoneme_type[i])
            syllable.add(phoneme)

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

    def get_word(self):
        result = []
        for phoneme in self.underlying_representation:
            result += phoneme.symbol

        return ''.join(result)
