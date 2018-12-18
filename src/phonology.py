from src.exceptions import InvalidSyllable, InvalidPhoneme


class Phonology(object):
    """
    :param phonemes: set
    :param valid_syllables: set of tuples {('C', 'V', 'C'), ... }
    """
    def __init__(self, phonemes, valid_syllables):
        self.phonemes = phonemes
        self.alphabet = self._get_alphabet()
        self.valid_syllables = valid_syllables

    def _get_alphabet(self):
        alphabet = set()
        for phoneme in self.phonemes:
            alphabet.add(phoneme.symbol)
        return alphabet

    def is_valid_word(self, word):
        for syllable in word.syllables:
            if not self.is_valid_syllable(syllable):
                raise InvalidSyllable(f"Word {word} contains invalid syllable {syllable.phonemes}")

        return True

    def is_valid_syllable(self, syllable):
        return syllable.structure in self.valid_syllables

    def add_phoneme(self, phoneme):
        if phoneme.symbol in self.alphabet:
            raise InvalidPhoneme(f"Phoneme {phoneme} invalid; symbol {phoneme.symbol} already in use.")
        self.phonemes.add(phoneme)

    def get_phonemes(self):
        for phoneme in self.phonemes:
            yield phoneme

    def add_syllable(self, syllable):
        self.valid_syllables.add(syllable)

    def get_syllables(self):
        for syllable in self.valid_syllables:
            yield syllable


class PhonologicalRule(object):
    def __init__(self):
        raise NotImplementedError


class Syllable(object):
    """
    The Syllable object defines the acceptable ways in which phonemes can be assembled to create a syllable.
    :param phonemes: the syllable as represented by Phoneme objects
    """
    def __init__(self, phonemes):
        self.phonemes = phonemes
        self.structure = self._parse_structure()

    def _parse_structure(self):
        structure = []
        for phoneme in self.phonemes:
            if isinstance(phoneme, Consonant):
                structure.append('C')
            elif isinstance(phoneme, Vowel):
                structure.append('V')
        return tuple(structure)


class Phoneme(object):
    def __init__(self, is_voiced, place, manner, symbol):
        self.is_voiced = is_voiced
        self.place = place
        self.manner = manner
        self.symbol = symbol


class Vowel(Phoneme):
    def __init__(self, is_voiced, place, manner, symbol, is_long):
        super().__init__(is_voiced, place, manner, symbol)
        self.is_long = is_long
        self.type = "V"


class Consonant(Phoneme):
    def __init__(self, is_voiced, place, manner, symbol):
        super().__init__(is_voiced, place, manner, symbol)
        self.type = "C"

