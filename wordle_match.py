#! /usr/local/bin/python3

"""
Date Created: 01/24/22
By: M Lassiter
Description: If user entered a guess-word, feedback on each character in the guess-word will be provided. If the first character in guess-word is NOT in hidden-word, an underscore will be appended to a new string in the first position (and move on to next character). If character in guess-word IS in hidden word, then need to check if its in correct position. If it IS in correct position, then character will be appeneded to new string in upper case. If NOT in correct position, then character will be appened to new string in lower case.

"""
import wordle

if __name__ == "__main__":
    print(wordle.wordle_match("chill", "large"))
    print(wordle.wordle_match("hello", "large"))
    print(wordle.wordle_match("hello", "label"))
    
