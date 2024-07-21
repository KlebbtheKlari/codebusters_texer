######
# Caesar cipher!
######

import re
from cipher_utils import *

def caesar_encode(s,shift):
    ret = ''
    l = list(s)
    
    for i in l:
        if (re.search("[a-zA-Z]",i)):
            i = i.upper()
            ret += num_to_letter(letter_to_num(i)+shift)
        else:
            ret += i
    return ret