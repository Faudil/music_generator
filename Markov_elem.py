import numpy as np

class Markov_elem:
    def __init__(self, word):
        self._word = word
        self._followings = []
        self._following_nbr = []
        self._following_proba = []

    def add_following(self, following_word):
        if following_word in self._followings:
            self._following_nbr[self._followings.index(following_word)] += 1
        self._followings.append(following_word)
        self._following_nbr.append(1)

    def calc_following_proba(self):
        all = sum(self._following_nbr)
        self._following_proba = []
        for nbr in self._following_nbr:
            self._following_proba.append(nbr / all)

    def pick_next(self):
        if not self._following_proba:
            raise Exception("Can't pick word without it's probability")
        return np.random.choice(self._followings, 1, p=self._following_proba)[0]

    def getword(self):
        return self._word