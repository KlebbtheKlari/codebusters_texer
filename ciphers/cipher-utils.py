import re

######
# Utility functions for cipher implementations
# Several of these are just renaming already known functions
# so they reflect more closely what it is I want in name
######

# removes repeated letters in a string
# input: string of letters in all caps (ex "EXAMPLE")
# output: same string with repeats removed (ex "EXAMPL")
# use cases: k1, k2, k3, fracmorse, polybius keys
def strip_repeats(s):
    return "".join(dict.fromkeys(s))

# removes all non-alphabetic characters from s
# capitalizes all letters of s
# input: a string
# output: "answerized" string (letters only, all caps)
# useful for ciphers w/ standardized block sizes
def answerize(s):
    regex = re.compile('[^a-zA-Z]')
    ret = regex.sub('',s)
    return ret.upper()\

# returns the modular inverse of a modulo m
def mod_inverse(a,m):
    return pow(a,-1,m)

# returns the corresponding letter for x
# using A=0, B=1, ... Z=25
# if x > 26, then letter is returned according to x mod 26
def A0Z25(x):
    return chr((x%26) + 65)
