#! /usr/local/bin/python3

import wordle


if __name__ == "__main__":
    wordle.word_match("happy", "happy")
    wordle.word_match("happy", "sad")
    wordle.word_match("happy", "12345")
    wordle.word_match("happy", "123")
    wordle.word_match("happy", "cheer")
