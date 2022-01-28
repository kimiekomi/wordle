#! /usr/local/bin/python3

import wordle

if __name__ == "__main__":
    print(wordle.track_letters(["happy", "aeiou", "HAPPY", "liars", "honey"], "honey"))
