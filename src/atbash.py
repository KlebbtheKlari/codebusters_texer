######
# Atbash cipher!
######

import re
from cipher_utils import *

class Atbash:
    pt = ''
    val = 0
    ct = ''
    
    def __init__(self, plaintext, value):
        self.pt = plaintext
        self.val = value
        self.ct = self.atbash_encode(plaintext)
    
    # TODO: return the entire texed version
    def __str__(self):
        return self.ct

    def atbash_encode(self, s):
        ret = ''
        l = list(s)
        
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += num_to_letter(25-letter_to_num(i))
            else:
                ret += i
        return ret
    
    def get_val(self):
        return self.val
    
    def get_ct(self):
        return self.ct
    
    def get_pt(self):
        return self.pt