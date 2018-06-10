import numpy as np

class Markov_elem:
    def __init__(self, note):
        self._note = note
        self._followings = []
        self._following_nbr = []
        self._following_proba = []

    def add_following(self, following_note):
        if following_note in self._followings:
            self._following_nbr[self._followings.index(following_note)] += 1
        self._followings.append(following_note)
        self._following_nbr.append(1)

    def calc_following_proba(self):
        all = sum(self._following_nbr)
        self._following_proba = []
        for nbr in self._following_nbr:
            self._following_proba.append(nbr / all)

    def pick_next(self):
        if not self._following_proba:
            raise Exception("Can't pick note without it's probability")
        return np.random.choice(self._followings, 1, p=self._following_proba)[0]

    def getNote(self):
        return self._note