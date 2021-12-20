# Author: Joshua Sia
# Date: 2021-12-19

'''This script fits a Markov language model a given corpus. The script
takes the path to a corpus and an optional n_gram argument specifying
where the size of n-gram to use.

Usage:
fit_model.py --in_corpus=<in_corpus> [--n_gram=<n_gram>]

Options:
--in_corpus=<in_corpus>     Path including filename specifying corpus
--n_gram=<n_gram>           Size of n-gram to use [default: 5]
'''

# python src/fit_model.py --in_corpus=data/corpus.txt --n_gram=5

import sys
from docopt import docopt
import numpy as np
from collections import defaultdict, Counter
import pickle

opt = docopt(__doc__)

def main(opt):

    if not(opt["--n_gram"].isnumeric()):
        sys.exit("n_gram argument should be an integer")

    n = int(opt["--n_gram"])

    with open(opt["--in_corpus"]) as f:
        text = f.read()

    # Make text circular so Markov chain doesn't get stuck
    circ_text = text + text[:n]

    # Compute transition matrix
    model = defaultdict(Counter)

    for idx, t in enumerate(text):
        t = circ_text[idx:idx+n]
        next_char = circ_text[idx+n]
        model[t].update(next_char)

    # Normalise frequencies in transition matrix to probabilities
    for key, value in model.items():
        denominator = sum(list(value.values()))
        for inner_key, inner_value in value.items():
            value[inner_key] = inner_value / denominator

    out_file = "results/" + opt["--in_corpus"][5:-4] + ".pickle"

    with open(out_file, "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
  main(opt)
