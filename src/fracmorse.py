######
# Fractionated Morse!
######

from cipher_utils import *

class Fracmorse:
    
    def __init__(self, type,val,plaintext,key,bonus,crib):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = plaintext.upper()
        self.key = answerize(key)
        self.ct = self.fracmorse_encode(self.pt, self.key)
        self.bonus = bonus # bool
        self.crib = answerize(crib)
        
    def fracmorse_encode(self,pt,key):
        ret = '' # string to be returned
        
        alphabet = gen_k_alphabet(key,0) # from aristocrat.py
        morse_string = to_morse(pt) # util
        
        # convert morse -> ternary
        morse_string = morse_string.replace('.','0')
        morse_string = morse_string.replace('-','1')
        morse_string = morse_string.replace('x','2')
        
        # pad extra x's at the end if needed
        while (len(morse_string) % 3 != 0):
            morse_string += '2'
        
        # read chars from alphabet using ternary
        for i in range(0,len(morse_string),3):
            x = int(morse_string[i])
            y = int(morse_string[i+1])
            z = int(morse_string[i+2])
            ret += alphabet[9*x+3*y+z]
        
        return ret
    
    # TODO: return the entire texed version
    def __str__(self):
        return self.ct
    
# f = Fracmorse('type',1,'card magic','sleight',False,'crib')
# print(f.ct)