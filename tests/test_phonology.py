from unittest import TestCase

from src.phonology import Consonant, Vowel, Syllable, Phonology


class TestPhonology(TestCase):

    def setUp(self):
        self.dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        self.tee = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')
        self.eye = Vowel(is_voiced=True, place={'high', 'front'}, manner='tense', symbol='i', is_long=True)

        phonemes = {self.dee, self.tee, self.eye}
        valid_syllables = {
            ('C', 'V', 'C'),
            ('C', 'V')
        }

        self.phonology = Phonology(phonemes, valid_syllables)

    def test_add_phoneme(self):
        dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        tee = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')

        test_phonemes = {dee, tee}

        phonology = Phonology(test_phonemes, valid_syllables=None)
        phonology.add_phoneme(dee)
        phonology.add_phoneme(tee)

        self.assertEqual(test_phonemes, phonology.phonemes)

    def test_validate_syllable(self):
        phonology = self.phonology
        good_syllable = Syllable([self.dee, self.eye, self.dee])
        bad_syllable = Syllable([self.eye, self.dee])

        self.assertTrue(phonology.validate_syllable(good_syllable))
        self.assertFalse(phonology.validate_syllable(bad_syllable))


class TestSyllable(TestCase):

    def test_parse_structure(self):
        dee = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
        eye = Vowel(is_voiced=True, place={'high', 'front'}, manner='tense', symbol='i', is_long=True)

        syllable = Syllable([dee, eye, dee])
        expected_structure = ('C', 'V', 'C')

        self.assertEqual(expected_structure, syllable.structure)
