#!/usr/bin/python3
import sys
import math
from collections import Counter

import pickle

from Markov_chain import Markov_chain

# this function use Shannon's Entropy formula
def calc_entropy(words, diff_words):
    occurences_words = Counter(words)
    entropy = 0
    nb_words = len(words)
    nb_diffwords = len(diff_words)
    for word in diff_words:
        prob = occurences_words[word] / nb_words
        entropy -= prob * math.log(nb_diffwords, prob)
    return entropy


def main(args):
    if len(args) != 3:
        return
    with open(args[0], "r", encoding="utf-8") as f:
        all = f.read()
        words = all.replace("\n", "").split(" ")
    if args[2] == "load":
        with open("saved.model", "rb") as f:
            mc = pickle.load(f)
    else:
        mc = Markov_chain()
        mc.compute_elems(words, all)
    if args[2] == "yes":
        with open("saved.model", "wb") as f:
            pickle.dump(mc, f)
    print("entropy of the text :", calc_entropy(words, set(words)))
    print("text generated : ", " ".join(mc.generateText(int(args[1]))))


if __name__ == "__main__":
    main(sys.argv[1:])

