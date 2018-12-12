
class Word(object):
    def __init__(self):
        self.underlying_representation = None


class Phonology(object):
    def __init__(self):
        self.phonemes = []
        self.rule_set = None


class PhonologicalRule(object):
    def __init__(self):
        raise NotImplemented


class Phoneme(object):
    def __init__(self, place, manner, voiced):
        self.place = place
        self.manner = manner
        self.voiced = voiced
