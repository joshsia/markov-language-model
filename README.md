# Markov language model

Author: Joshua Sia

Personal project inspired from UBC Master of Data Science Course DSCI 521.

### About

A Markov model of an input text known as a corpus is learned and can be used to synthesise text. The model learns all possible *n*-grams in the corpus as well as the possible characters that can follow a given *n*-gram. A random text of specified length can then be generated one character at a time from the learned model.

### Usage

There are two suggested ways to run this analysis:

#### 1\. Using Docker

*note - the instructions in this section also depends on running this in
a unix shell (e.g., terminal or Git Bash)*

To replicate the analysis, install
[Docker](https://www.docker.com/get-started). To pull the [Docker image](https://hub.docker.com/repository/docker/joshsia/markov-language-model) from Docker Hub, run the following command:

```
docker pull joshsia/markov-language-model
```

Clone this GitHub repository and run the following command at the command line/terminal
from the root directory of this project (Mac M1 users should add the flag and value `--platform linux/amd64`, and Windows users should use `//` in the path):

```
docker run --rm -it -v /$(pwd):/home joshsia/markov-language-model make -C /home all
```

To reset the project to a clean state with no intermediate files, run the following command at the command line/terminal from the root directory of this project (Mac M1 users should add the flag and value `--platform linux/amd64`, and Windows users should use `//` in the path):

```
docker run --rm -it -v /$(pwd):/home joshsia/markov-language-model make -C /home clean
```

#### 2\. Without using Docker

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
