######
# Affine cipher!
######

import re
from cipher_utils import *

def affine_encode(s,A,B):
    ret = ''
    l = list(s)
    
    for i in l:
        if (re.search("[a-zA-Z]",i)):
            i = i.upper()
            ret += num_to_letter(A*letter_to_num(i)+B)
        else:
            ret += i
    return ret