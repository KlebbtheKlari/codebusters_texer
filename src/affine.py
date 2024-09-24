######
# Affine cipher!
######

import re
from cipher_utils import *

class Affine:
    # string pt, string ct, int val, tuple (int,int) key
    
    def __init__(self, type, plaintext, value, keyA, keyB, bonus, crib=None):
        self.type = type
        self.pt = plaintext
        self.val = value
        self.key = (int(keyA), int(keyB))
        self.ct = self.affine_encode(plaintext, self.key[0], self.key[1])
        self.bonus = bonus
        
        if (crib == None):
            pass
        else:
            self.crib = crib

    def affine_encode(self,s,A,B):
        ret = ''
        l = list(s)
        
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += num_to_letter(A*letter_to_num(i)+B)
            else:
                ret += i
        return ret
    
    # TODO: return the entire texed version
    def __str__(self):
        return self.ct

# a = Affine('type','plaintext',12,'11','3',False)
# print(a)