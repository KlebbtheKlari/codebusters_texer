######
# Utility functions for cipher implementations
# Several of these are just renaming already known functions
# so they reflect more closely what it is I want in name
######

import re
import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    return ret.upper()


# returns the modular inverse of a modulo m
def mod_inverse(a,m):
    return pow(a,-1,m)


# returns the corresponding letter for x
# using A=0, B=1, ... Z=25
# if x > 26, then letter is returned according to x mod 26
def A0Z25(x):
    return chr((x%26) + 65)

def num_to_letter(x):
    return A0Z25(x)

# returns the corresponding number for x
# using A=0, B=1, ... Z=25
# input: x is a single upper-case letter
def letter_to_num(x):
    return (ord(x)-65)


# returns the corresponding numbers for a string s
# input: string
# output: list of numbers corresponding letter-by-letter of s
def string_to_nums(s):
    letters = answerize(s)
    ret = []
    for i in list(letters):
        ret.append(letter_to_num(i))
    return ret


# returns s split into blocks of length size
# input: string, int
# output: string
def blockify(s,size):
    ret = ''
    for i in range(len(s)):
        ret += s[i]
        if (i%size == size-1):
            ret += " "
    return ret

morse = {'A':'.-',
         'B':'-...',
         'C':'-.-.',
         'D':'-..',
         'E':'.',
         'F':'..-.',
         'G':'--.',
         'H':'....',
         'I':'..',
         'J':'.---',
         'K':'-.-',
         'L':'.-..',
         'M':'--',
         'N':'-.',
         'O':'---',
         'P':'.--.',
         'Q':'--.-',
         'R':'.-.',
         'S':'...',
         'T':'-',
         'U':'..-',
         'V':'...-',
         'W':'.--',
         'X':'-..-',
         'Y':'-.--',
         'Z':'--..',
         '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----',
         ' ':''
         }
# converts s to morse code 
def to_morse(s):
    s = s.upper()
    ret = ''
    for i in list(s):
        if (re.search("[a-zA-Z ]",i)):
            i = i.upper()
            ret += morse[i]
            ret += 'x'
    return ret

# generates a random alphabet
# ensures that no letter is in the same position
# as in the normal alphabet
def gen_random_alphabet():
    l = list(alphabet)
    alpha = list(alphabet)
    fixed = False
    
    while(not fixed):
        fixed = True
        random.shuffle(alpha)
        for i in range(len(alpha)):
            if alpha[i] == l[i]:
                fixed = False
    
    return ''.join(alpha)


# generate K alphabet with key & shift
def gen_k_alphabet(key,shift):
    # circular shift string fwd by shift
    def circle_shift(s):
        ns = ''
        for i in range(-shift,-shift+26):
            ns += s[i%26]
        return ns
    
    s = strip_repeats(key)
    for i in list(alphabet):
        if (i not in list(s)):
            s += i
    s = circle_shift(s)
    return s


# Converts letter -> bacon string in As and Bs
def baconify(s):
    ret = ''
    a = letter_to_num(s)
    if (a >= 9):
        a -= 1
    if (a >= 20):
        a -= 1
    for i in range(5):
        ret += str(a%2)
        a = a//2
    return ret[::-1]