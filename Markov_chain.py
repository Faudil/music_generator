import random

from Markov_elem import Markov_elem

class Markov_chain:
    def __init__(self):
        self._elems = {}

    def compute_elems(self, notes):
        self._diff_notes = list(set(notes))
        self._elems = dict({note : Markov_elem(note) for note in self._diff_notes})
        l = len(notes)
        for i in range(0, l - 1):
            self._elems[notes[i]].add_following(notes[i + 1])
        for v in self._elems.values():
            v.calc_following_proba()

    def composeMusic(self, size):
        t = self._diff_notes[random.randint(0, len(self._elems) - 1)]
        elem = self._elems[t]
        music = []
        for i in range(0, size):
            note = elem.pick_next()
            music.append(note)
            elem = self._elems[note]
        return music





