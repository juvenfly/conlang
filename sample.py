from src.lexicon import Lexicon
from src.phonology import Phonology, Consonant, Vowel


def main():
    """
    This sample script builds the phonology for Central Rotokas and generates a phonologically valid lexicon.
    :return:
    """
    phonemes = build_phonemes()
    phonology = build_phonology(phonemes)

    lexicon = Lexicon(phonology)
    lexicon.generate_lexicon()

    print(lexicon.word_list)


def build_phonemes():

    # consonants
    p = Consonant(is_voiced=False, place='bilabial', manner='stop', symbol='p')
    t = Consonant(is_voiced=False, place='alveolar', manner='stop', symbol='t')
    k = Consonant(is_voiced=False, place='velar', manner='stop', symbol='k')

    b = Consonant(is_voiced=True, place='bilabial', manner='stop', symbol='b')
    d = Consonant(is_voiced=True, place='alveolar', manner='stop', symbol='d')
    g = Consonant(is_voiced=True, place='velar', manner='stop', symbol='g')

    b_fric = Consonant(is_voiced=True, place='bilabial', manner='fricative', symbol='β')
    r = Consonant(is_voiced=True, place='alveolar', manner='tap', symbol='r')
    g_fric = Consonant(is_voiced=True, place='velar', manner='fricative', symbol='ɣ')

    # vowels
    i = Vowel(is_voiced=True, place={'close', 'front'}, manner='tense', is_long=False, symbol='i')
    long_i = Vowel(is_voiced=True, place={'close', 'front'}, manner='tense', is_long=True, symbol='i:')
    e = Vowel(is_voiced=True, place={'close-mid', 'front'}, manner='tense', is_long=False, symbol='e')
    long_e = Vowel(is_voiced=True, place={'close-mid', 'front'}, manner='tense', is_long=True, symbol='e:')
    a = Vowel(is_voiced=True, place={'open', 'front'}, manner='lax', is_long=False, symbol='a')
    long_a = Vowel(is_voiced=True, place={'open', 'front'}, manner='lax', is_long=True, symbol='a:')
    u = Vowel(is_voiced=True, place={'close', 'back'}, manner='lax', is_long=False, symbol='u')
    long_u = Vowel(is_voiced=True, place={'close', 'back'}, manner='lax', is_long=True, symbol='u:')
    o = Vowel(is_voiced=True, place={'close-mid', 'back'}, manner='lax', is_long=False, symbol='o')
    long_o = Vowel(is_voiced=True, place={'close-mid', 'back'}, manner='lax', is_long=True, symbol='o:')

    phonemes = {p, t, k, b, d, g, b_fric, r, g_fric, i, long_i, e, long_e, a, long_a, u, long_u, o, long_o}

    return phonemes


def build_phonology(phonemes):
    valid_syllable_structures = {
        ('V',),
        ('C', 'V')
    }

    return Phonology(phonemes, valid_syllable_structures)


if __name__ == "__main__":
    main()
