######
# Atbash cipher!
######

import re
from cipher_utils import *

class Atbash:
    pt = ''
    ct = ''
    
    def __init__(self, plaintext):
        self.pt = plaintext

    def atbash_encode(s):
        ret = ''
        l = list(s)
        
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += num_to_letter(25-letter_to_num(i))
            else:
                ret += i
        return ret