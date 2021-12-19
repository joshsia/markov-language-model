# Author: Joshua Sia
# Date: 2021-12-19
#
# Driver script for pipeline of Markov language model
#
# Usage:
# make all

all : results/synthetic_corpus.txt

# Download corpus
data/corpus.txt :
	python src/get_corpus.py --url=http://www.gutenberg.org/files/2591/2591-0.txt --start=2820 

# Fit Markov model
results/corpus.pickle : data/corpus.txt
	python src/fit_model.py --in_corpus=data/corpus.txt --n_gram=5

# Generate synthetic text
results/synthetic_corpus.txt : results/corpus.pickle
	python src/generate_text.py --in_model=results/corpus.pickle --len=500

clean :
	rm -rf results/*
	rm -rf data/*