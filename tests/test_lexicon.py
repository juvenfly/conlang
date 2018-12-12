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

    def test_print_word(self):
        expected_word = 'dittit'
        actual_word = self.test_word.get_word()

        self.assertEqual(expected_word, actual_word)
