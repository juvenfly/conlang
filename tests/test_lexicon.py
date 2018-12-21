from unittest import TestCase

from src.lexicon import Word
from src.phonology import Consonant, Vowel, Syllable


class TestWord(TestCase):

    def setUp(self):
        self.dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        self.tee = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')
        self.eye = Vowel(is_voiced=True, place={'high', 'front'}, manner='tense', symbol='i', is_long=True)

        syllables = [
            Syllable([self.dee, self.eye, self.tee]),
            Syllable([self.tee, self.eye, self.tee])
        ]
        self.test_word = Word(syllables)

    def test_get_surface_representation(self):
        expected_surface_repr = 'dittit'
        actual_surface_repr = self.test_word.surface_representation

        self.assertEqual(expected_surface_repr, actual_surface_repr)

    def test_get_underlying_representation(self):
        underlying_repr = self.test_word.underlying_representation
        self.assertTrue(isinstance(underlying_repr, tuple))
        self.assertEqual(len(underlying_repr), 6)
