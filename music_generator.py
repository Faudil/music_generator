#!/usr/bin/python3
import sys
import math
from collections import Counter

from Markov_chain import Markov_chain

# this function use Shannon's Entropy formula
def calc_entropy(notes, diff_notes):
    occurences_notes = Counter(notes)
    entropy = 0
    nb_notes = len(notes)
    nb_diffnotes = len(diff_notes)
    for note in diff_notes:
        prob = occurences_notes[note] / nb_notes
        entropy -= prob * math.log(nb_diffnotes, prob)
    return entropy


def main(args):
    if len(args) != 2:
        return
    with open(args[0], "r") as f:
        notes = f.read().replace("\n", "").split(" ")
    mc = Markov_chain()
    mc.compute_elems(notes)
    print("entropy of the music :", calc_entropy(notes, set(notes)))
    print("music generated", mc.composeMusic(int(args[1])))


if __name__ == "__main__":
    main(sys.argv[1:])

