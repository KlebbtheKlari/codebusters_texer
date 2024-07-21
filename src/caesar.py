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
        else:
            self.shift = sh
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
        return self.ct
