from typing import Sequence

def break_words(List_stuff):
    print(">>", List_stuff)
    words = List_stuff.split(' ')
    print (words)
    return words

def sort_words(words):
    print(">>", words)
    print(sorted(words))
    return sorted(words)

def print_first_word(words):
    word=words.pop(0)
    print(word)

def print_last_word(words):
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last_sentence(sentence):
    words= break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

a = ["champ", "is", "here"]
b = "always is and forever"
list_to_break =  "champ was here yesterday"


break_words(list_to_break)
sort_words(a)
#sort_words(b)
#print_first_word(b)
#print_first_and_last_sorted(b)

#Sorts.. sorts alphabetically
sorted(a)
print (sorted(a))