"""
This file provides functions to brute force weak ciphers

All brute force methods need to be able to work with spaces and no spaces

TODO:
    - Add threading on Vigenere brute force

"""
import time
import ciphers
from english_dictionary.scripts.read_pickle import get_dict
import itertools
import threading
import sys
import os
#import alert

global tolerance
tolerance=0.8

def caesar(text, return_type="bg"):
    """
    Brute forces the caesar cipher
    Takes a string text and an optional string return_type

    return_type can be: 
        bg "best guess" (the version which has the most real words in it)
        all "all" (a list of all of the possible solutions)

    In bg mode, returns the best guess, which is the string with the most instances of real words
    If there are two strings with the same amount of instances 

    TODO:
        - Also return the key which was used to encrypt the text
        - Allow passing which wordlist to use

    """

    global tolerance

    # A list of the text encrypted which each possible key for caesar cipher
    test_texts=[]
    for i in range(1,26):
        test_texts.append(ciphers.caesar(text, i))
    
    # Creates an object for testing if a text is a word or is ciphertext
    realTest = ciphers.realEngine("small_specialized")
    
    # These two variables (best_guess) get replaced with the current tested string if the string had more real words in it that the current best_guess_count, counts is used to track how many real words are in each permutation of ciphertext
    best_guess_string=""
    best_guess_count=-1
    counts=[]

    for i in test_texts:
        count=0
        test=i.split()

        for j in test:
            if realTest.plaintext_or_ciphertext(j):
                count+=1
        if count>best_guess_count:
            best_guess_string=i
            best_guess_count=count
        counts.append(count)

    if realTest.plaintext_or_ciphertext(best_guess_string, tolerance):
        return(best_guess_string)
    return(False)
    
def vigenere(text, keycode="w", length=None):
    """
    Based on flags, encrypts with all versions of a keyspace or english words

    Runs through db to find most likely match

    flags:
        - w : english words
        - l : english letters
    """

    global tolerance
    
    realTest = ciphers.realEngine("small_specialized")

    keys=[]

    if "w" in keycode:
        for i in get_dict():
            if len(i)>0:
                keys.append(i)
    if "l" in keycode:
        lower="abcdefghijklmnopqrstuvwxyz"
        combinations = itertools.product(lower, repeat=length)
        for combo in combinations:
            keys.append(''.join(combo))

    def calculate_square(text, key):
        tr=ciphers.vigenere(text, key, "d")

        if realTest.plaintext_or_ciphertext(tr, tolerance):

            ciphers.writeToDatabase("vigenere", (key, ciphers.vigenere(text, key, "d")))

    threads = []

    for i in keys:
        thread = threading.Thread(target=calculate_square, args=(text, i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def substitution(text):
    #print("substitution")

    global tolerance

    return(False)

def railfence(text):
    global tolerance

    realTest = ciphers.realEngine("small_specialized")

    for i in range(2,200):
        test=(ciphers.rail_fence(text, i, "d"))
        if realTest.plaintext_or_ciphertext(test, tolerance):
            return(test, i)
        
    return(False)
