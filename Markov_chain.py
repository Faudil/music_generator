#!/usr/bin/python3
import random

import keras as ks
import numpy as np

from Markov_elem import Markov_elem

class Markov_chain:
    def __init__(self):
        self._elems = {}

    def compute_elems(self, words, all):
        self._sentences = [s for s in ks.preprocessing.text.text_to_word_sequence(all, filters='\t"()#$%&()*+-/:;<=>@[\]^_`{|}~', lower=True, split='.!?;')]
        words = ks.preprocessing.text.text_to_word_sequence(all, filters='\t!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True, split=' ')
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

    def isclose(self, sentence):
        words = ks.preprocessing.text.text_to_word_sequence(sentence, filters='\t!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True, split=' ')
        dist = 0
        l = len(words)
        for i in range(0, l - 1):
            if words[i] in self._elems:
                dist += 1 - self._elems[words[i]].get_following_proba(words[i + 1])
        return dist


