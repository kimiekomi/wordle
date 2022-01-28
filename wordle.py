#! /usr/bin/python3

import sys
import random
import string

debug = False
trace = False

Wordle_File_Name = "five_letter_words.txt"

def wordle(word_list, test_word=None):

    if debug: print(f"wordle (partial_word_list={word_list[0:10]}, test_word={test_word})\n")

    if test_word != None:
        secret_word = test_word
    else:
        secret_word = random_word(word_list)

    if debug: print (f"secret_word = {secret_word}")

    file = open("word_history.txt", "a")

    file.write(secret_word + "\n")

    file.close()
    
    if trace: print(f"  secret_word = '{secret_word}'")

    guess_word_list = []
    feedbacks = []

    number_of_attempts = 6

    for attempt in range(number_of_attempts):

        while True:
            guess_word = input("Guess: ")

            if len (guess_word) != len(secret_word):
                print (f"Guess must be {len(secret_word)} letters")
                letter_status (guess_word_list, secret_word)
                status (guess_word_list, feedbacks)
                continue

            if not word_search(guess_word, word_list):
                print(f"Enter a valid {len(secret_word)}-letter word")
                letter_status (guess_word_list, secret_word)
                status (guess_word_list, feedbacks)
                continue

            guess_word_list.append (guess_word)
            break

        feedback = wordle_match(guess_word, secret_word)
        feedbacks.append (feedback)

        print ()

        letter_status (guess_word_list, secret_word)
        status (guess_word_list, feedbacks)

        print (f"{number_of_attempts-attempt-1} guesses remaining\n")
    
        if feedback == secret_word.upper():
            print("Alright! You've guessed the hidden word!")
            return

    print(f"Sorry, the correct word was '{secret_word}'") 


def status (guesses, feedbacks):

    for i in range (len (guesses)):
        print(f"'{guesses[i]}' : '{feedbacks[i]}'")

    print ()


def letter_status (guesses, secret):

    used_letters = []
    unused_letters = []

    used_letters, unused_letters = track_letters(guesses, secret)

    for letter in used_letters:
        if letter in secret:
            used_letters = used_letters.replace(letter, letter.upper())

    print (f"     Used letters: {used_letters}")
    print (f"Remaining letters: {unused_letters}")
    print ()


def load_dictionary(file_name):

    if debug: print (f"word_catalog called")

    file = open(file_name, "r") 

    lines = file.readlines()

    file.close()
    
    word_list = []

    for word in lines:
        word = word.strip()
        word_list.append(word)

    return word_list


def random_word(dictionary):

    random_index = random.randrange(len(dictionary))

    if trace: print(f"  words[random_index] = {dictionary[random_index]}")

    return dictionary[random_index].strip()


def wordle_match(guess_word, secret_word):

    if len (guess_word) != len(secret_word): raise "oh you blew it"

    feedback = ""
    secret_word_list = list(secret_word)

    if trace: print (secret_word_list)

    for i in range(len(guess_word)):
        this_letter = guess_word[i]

        if not this_letter in secret_word_list:
            feedback += "_"
            continue

        if this_letter == secret_word [i]:
            feedback += this_letter.upper()

        else:
            feedback += guess_word[i].lower()

        try:
            index = secret_word_list.index (this_letter)
            secret_word_list.pop (index)
            
            if trace: print (secret_word_list)

        except:
            pass

        if trace: print(f"feedback - {feedback}")
    
    return feedback


def word_search (word, dictionary):

    if debug: print (f"word_search('{word}', {dictionary[0:5]}...)")

    for entry in dictionary:

        if word_match (word, entry):
            return True

    if debug: print (f"word_search returns False")

    return False


def word_match(string_1, string_2):

#     if debug: print(f"word_match ('{string_1}', '{string_2}')")

    if len(string_1) != len(string_2):
        if trace: print(f"length of '{string_1}' does NOT match length of '{string_2}'")
        return False
	
    for i in range(len(string_1)):

        if trace: print(f"comparing '{string_1[i]}' with '{string_2[i]}'")

        if string_1[i] != string_2[i]:
            if trace: print(f"'{string_1}' does NOT match '{string_2}'")
            return False

    if trace: print(f"'{string_1}' does match '{string_2}'")

    return True


def track_letters(guesses, secret_word):

    if debug: print(f"track_letters(guesss='{guesses}', hidden='{secret_word}')")

    used_letters = []
    unused_letters = list(string.ascii_lowercase)

    for guess_word in guesses:
        guess_word = guess_word.lower()
        
        for i in range(len(guess_word)):
            letter = guess_word[i]

            if trace: print(f"  checking '{letter}'")

            if letter in used_letters:
                continue

            if trace: print(f"moving {letter} from unused to used")

            index = unused_letters.index(letter)
            letter = unused_letters.pop(index)
             
            used_letters += letter

    used_letters = ''.join(sorted(used_letters))
    unused_letters = "".join(unused_letters)

    if debug: print(f"track_letters returning (used_letters='{used_letters}', unused_letters='{unused_letters}'")

    return used_letters, unused_letters


if __name__ == "__main__":

    word_list = load_dictionary(Wordle_File_Name)

    if len(sys.argv) > 1:
        # debug = True
        test_words = sys.argv[1:]

        for test_word in test_words:
            wordle (word_list, test_word)

    else:

        while True:
            wordle(word_list)

            response = input ("\nWould you like to play again? ")

            if response != "y" and response != "yes":
                break

            print ("\n\n")

        print ("Okay... Be like that!")
