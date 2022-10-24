
from typing import Sequence


def break_words(stuff):
    """This function will break up words for us."""
    print(">>> stuff =", stuff)
    words = stuff.split(' ')
    print("<<< Exiting break_words")
    return words

def sort_words(words):
    """Sorts the words."""
    print(">>> words =", words)
    print("<<< Exiting .. sort_words")
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    print(">>> words =", words)
    word = words.pop(0)
    print(word)
    print(">>> Exit print_first_word")

def print_last_word(words):
    """Prints the last words after popping it off."""
    print(">>> word =", words)
    word = words.pop(-1)
    print(">>> Exit print_last_word")
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    print("<<< sentence =", sentence)
    #called a function inside another function
    words = break_words(sentence)
    print(">>> Exit sort_sentence")
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    #called other  functions inside this function
    print(">>> sentence =", sentence)
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< Exit print_first_and_last")

def print_first_and_last_sorted(sentence):
    """Sorts words, then prints the first and last one."""
    #called other  functions inside this function
    print(">>> sentence =", sentence)
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< Exit print_first_and_last_sorted")

print_first_and_last_sorted("You are on your own man")


