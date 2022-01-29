#! /usr/bin/env python3

import sys
from wordle import load_dictionary, word_search

debug = True
trace = False

# def main(command_line_arguments):

#     if debug: print (f"main called with: {command_line_arguments}")

#     file = open("five_letter_words.txt", "r") 

#     lines = file.readlines()

#     file.close()
    
#     word_list = []

#     for word in lines:
#         word = word.strip()
#         word_list.append(word)

#     if trace: print(f"\nfirst ten words: {word_list[0:10]}\n")

#     command_line_arguments = command_line_arguments[1:]

#     for argument in command_line_arguments:
#         word = argument.lower()

#         is_found = word_search(word, word_list)

#         if is_found:
#             print(f"'{word}' was found")

#         else:
#             print(f"'{word}' was NOT found")
                
#     if len(command_line_arguments) == 0:
#         print("Enter at least one word to search for")


# def word_search (word, dictionary):

#     if debug: print (f"word_search('{word}', {dictionary[0:5]}...)")

#     for entry in dictionary:

#         if wordle.word_match (word, entry):
#             return True

#     if debug: print (f"word_search returns False")

#     return False


if __name__ == "__main__":

    word_list = load_dictionary ("five_letter_words.txt")

    # print (word_list)

    if len (sys.argv) == 1:
        print (word_search("zzzzz", word_list))
        print (word_search("aahed", word_list))
        print (word_search("happy", word_list))

    else:
        print (word_search(sys.argv[1], word_list))
