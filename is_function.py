#!/usr/bin/python
# checks if an integer is a integer including 7.0
def is_int(x):
    if x is int or x - floor(x) == 0:
        return True
    else:
        return False

# checks if an integer is even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
# adds all digits in a number
def digit_sum(n):
    tot = 0
    while n > 0:
        y = n % 10
        n = n - y
        tot = tot + y
        n = n // 10
    return tot
print digit_sum(1256)
# Factorial of a number
def factorial(x):
    if x == 1:
        return 1
    else:
        return (factorial(x - 1)) * x
# check an integer if it is prime

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        else:
            return True
# first way figured out to reverse a string
def reverse(text):
    results = []
    for i in text:
        results.append(i)
    count = len(results) - 1
    text = ""
    while count >= 0:
        text = text + results[count]
        count -= 1
        
    return text
# reverses a String
def reverse(text):
    newText = ""
    for n in range(len(text)-1, -1, -1):
        newText = newText + text[n]
    return newT
# returns a string given w/out the vowels
def anti_vowel(text):
    results = ""
    for n in text:
        if n not in "aeiouAEIOU":
            results = results + n
    return results

#finds the score of a scrabble word without board modifiers
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
        
def scrabble_score(word):
    word = word.lower()
    results = 0
    for n in word:
        results = results + score[n]
    return results

# censor a sentence with a word of your choosing
#def censor(text, word):
#    splitter = text.split()
#    for i in range(0, len(splitter)):
#        if splitter[i] == word:
#            splitter[i] = "*" * len(splitter[i])
#    return " ".join(splitter)def censor(text, word):
#    splitter = text.split()
#    for i in range(0, len(splitter)):
#        if splitter[i] == word:
#            splitter[i] = "*" * len(splitter[i])
#    return " ".join(splitter)
#count the number of times an item occurs in a list
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
            
    return count
# median of a list\
def median(s):
    med = 0
    s = sorted(s) 
    if len(s) % 2 == 0:
        med = ((s[len(s) / 2 - 1]) + (s[len(s) / 2])) / 2.0
    else:
        med = int(s[len(s) / 2])
    return med
#list comprehesions example
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,12) if (x**2) % 2 == 0]

print even_squares

#more with list comprehensions
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
print cubes_by_four
