# Author: Joshua Sia
# Date: 2021-12-19

'''This script generates a text file from a learned Markov model of
a corpus. The script takes the learned model, and an optional
filename to save as.

Usage:
generate_text.py --in_model=<in_model> [--len=<len>] [--out_file=<out_file>]

Options:
--in_model=<in_model>       Filename of learned model
--len=<len>                 Length of generated text [default: 200]
--out_file=<out_file>       Filename to save corpus as [default: corpus.txt]
'''

# python src/generate_text.py --in_model=results/corpus.pickle --len=200 --out_file=corpus

import sys
from docopt import docopt
import pickle
import numpy as np

opt = docopt(__doc__)

def main(opt):

    if not(opt["--len"].isnumeric()):
        sys.exit("len argument should be an integer")

    with open(opt["--in_model"], "rb") as f:
        model = pickle.load(f)

    out_text = next(iter(model))
    n = len(out_text)

    while len(out_text) < int(opt["--len"]):
        current_ngram = out_text[-n:]
        inner_dict = model[current_ngram]

        generated_char = np.random.choice(
            list(inner_dict.keys()),
            p=list(inner_dict.values())
            )
        
        out_text += generated_char
    
    out_file = "results/" + opt["--out_file"]
    with open(out_file, "w") as f:
        f.write(out_text)


if __name__ == "__main__":
  main(opt)