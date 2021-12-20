# Markov language model

Author: Joshua Sia

Personal project inspired from UBC Master of Data Science Course DSCI 521.

### About

A Markov model of an input text, known as a corpus, is learned and can be used to synthesise text. The model learns all possible *n*-grams in the corpus as well as the possible characters that can follow a given *n*-gram. A random text of specified length can then be generated one character at a time from the learned model.

### Usage

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following command at the command line/terminal from the root directory of this project:

 ```
 make all
 ```

To reset the project to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

 ```
 make clean
 ```

### Dependencies

- Python version 3.9.5 and Python packages:
    -   docopt=0.6.2
    -   numpy=1.21.2
