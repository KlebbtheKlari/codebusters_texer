######
# Caesar cipher!
######

import re
from cipher_utils import *
from random import randint

class Caesar:
    def __init__(self, plaintext, value, sh=None):
        self.pt = plaintext
        self.val = value
        if (sh == None):
            self.shift = randint(3,23)
            self.crib = False
        else:
            self.shift = int(sh)
            self.crib = True
        self.ct = self.caesar_encode(plaintext, self.shift)
        
    def caesar_encode(self,s,shift):
        ret = ''
        l = list(s)
        
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += num_to_letter(letter_to_num(i)+shift)
            else:
                ret += i
        return ret
    
    # TODO: return the entire texed version
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Caesar}} cipher'.format(42)
        
        # if a crib exists, add it
        if (self.crib):
            ret += ' with a shift of '
            ret += str(self.shift())
        ret += '.'
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breaklines]'.format(42)
        ret += '\n'
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret
