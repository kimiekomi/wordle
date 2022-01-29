#! /usr/bin/env python3

import sys
from wordle import load_dictionary, word_search

debug = True
trace = False

if __name__ == "__main__":

    word_list = load_dictionary ("five_letter_words.txt")

    if len (sys.argv) == 1:
        print (word_search("zzzzz", word_list))
        print (word_search("aahed", word_list))
        print (word_search("happy", word_list))

    else:
        print (word_search(sys.argv[1], word_list))
