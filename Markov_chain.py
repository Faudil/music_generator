#!/usr/bin/python3
import random

import keras as ks
import numpy as np

from Markov_elem import Markov_elem

class Markov_chain:
    def __init__(self):
        self._elems = {}

    def compute_elems(self, words, all):
        self._sentences = [str(s[0]) for s in ks.preprocessing.text.text_to_word_sequence(all, filters='\t"()#$%&()*+-/:;<=>@[\]^_`{|}~', lower=True, split='.!?;')]
        words = ks.preprocessing.text.text_to_word_sequence(all, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True, split=' ')
        self._diff_words = list(set(words))
        self._elems = dict({word : Markov_elem(word) for word in self._diff_words})
        l = len(words)
        for i in range(0, l - 1):
            self._elems[words[i]].add_following(words[i + 1])
        for v in self._elems.values():
            v.calc_following_proba()

    def generateText(self, size):
        t = self._diff_words[random.randint(0, len(self._elems) - 1)]
        elem = self._elems[t]
        text = [np.random.choice(self._sentences)]
        for i in range(0, size - 1):
            word = elem.pick_next()
            text.append(word)
            elem = self._elems[word]
        return text





