from random import *
class Word:
    #In this class we declare the list of words wich we are going to use to play

    def __init__(self):
        #This is the list and we will use only one word at a time.
        self._word = ["blue", "green", "orange", "black", "purple", "Brown"] 

    def get_random_word(self):
        #This function will return a random word from the list
        self._index = randint(0, 6)
        return self._word[self._index]