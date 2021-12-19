# Author: Joshua Sia
# Date: 2021-12-19

'''This script downloads a text file from a given URL. The script
takes a URL, the filename to save as, and an optional start argument
specifying where the text starts from.

Usage:
get_corpus.py --url=<url> --out_file=<out_file> [--start=<start>]

Options:
--url=<url>             URL to download text from
--out_file=<out_file>   Filename to save corpus as [default: corpus]
--start=<start>         Integer specifying where the text starts [default: 0]
'''

# python src/get_corpus.py --url=http://www.gutenberg.org/files/2591/2591-0.txt --out_file=grimms_fairy_tales --start=2820

import sys
from docopt import docopt
import urllib.request

opt = docopt(__doc__)

def main(opt):
  
  if not(opt["--start"].isnumeric()):
    sys.exit("Start argument should be an integer")

  corpus = urllib.request.urlopen(opt["--url"]).read().decode("utf-8")
  corpus = corpus[int(opt["--start"]):]

  out_file = "data/" + opt["--out_file"] + ".txt"

  with open(out_file, 'w') as f:
    f.write(corpus)

if __name__ == "__main__":
  main(opt)