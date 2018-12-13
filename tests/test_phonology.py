from unittest import TestCase

from src.exceptions import InvalidSyllable
from src.phonology import Consonant, Vowel, Syllable, Phonology
from src.lexicon import Word


class TestPhonology(TestCase):

    def setUp(self):
        self.dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        self.tee = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')
        self.eye = Vowel(is_voiced=True, place={'high', 'front'}, manner='tense', symbol='i', is_long=True)

        phonemes = {self.dee, self.tee, self.eye}
        valid_syllable_structures = {
            ('C', 'V', 'C'),
            ('C', 'V')
        }

        self.phonology = Phonology(phonemes, valid_syllable_structures)

        syllables = [
            Syllable([self.dee, self.eye, self.tee]),
            Syllable([self.tee, self.eye, self.tee])
        ]

        invalid_syllables = [
            Syllable([self.eye, self.tee]),
            Syllable([self.eye, self.tee])
        ]

        self.good_word = Word(syllables)
        self.invalid_word = Word(invalid_syllables)

    def test_add_phoneme(self):
        dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        tee = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')

        test_phonemes = {dee, tee}

        phonology = Phonology(test_phonemes, valid_syllables=None)
        phonology.add_phoneme(dee)
        phonology.add_phoneme(tee)

        self.assertEqual(test_phonemes, phonology.phonemes)

    def test_is_valid_word(self):
        self.assertTrue(self.phonology.is_valid_word(self.good_word))
        self.assertRaises(InvalidSyllable, self.phonology.is_valid_word, self.invalid_word)

    def test_is_valid_syllable(self):
        phonology = self.phonology
        good_syllable = Syllable([self.dee, self.eye, self.dee])
        bad_syllable = Syllable([self.eye, self.dee])

        self.assertTrue(phonology.is_valid_syllable(good_syllable))
        self.assertFalse(phonology.is_valid_syllable(bad_syllable))


class TestSyllable(TestCase):

    def test_parse_structure(self):
        dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        eye = Vowel(is_voiced=True, place={'high', 'front'}, manner='tense', symbol='i', is_long=True)

        syllable = Syllable([dee, eye, dee])
        expected_structure = ('C', 'V', 'C')

        self.assertEqual(expected_structure, syllable.structure)
