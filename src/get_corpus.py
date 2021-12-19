# Author: Joshua Sia
# Date: 2021-12-19

'''This script downloads a text file from a given URL. The script
takes a URL and an optional start argument specifying where the 
text starts from.

Usage:
get_corpus.py --url=<url> [--start=<start>]

Options:
--url=<url>             URL to download text from
[--start=<start>]       Integer specifying where the text starts
'''

# python src/get_corpus.py --url=http://www.gutenberg.org/files/2591/2591-0.txt --start=2820

import sys
from docopt import docopt
import urllib.request

opt = docopt(__doc__)

def main(opt):

  if not(opt["--start"].isnumeric()):
    sys.exit("Start argument should be an integer")

  corpus = urllib.request.urlopen(opt["--url"]).read().decode("utf-8")
  corpus = corpus[int(opt["--start"]):]

  with open('data/corpus.txt', 'w') as f:
    f.write(corpus)

if __name__ == "__main__":
  main(opt)