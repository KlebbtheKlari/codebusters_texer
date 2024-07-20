######
# Atbash cipher!
######

import re
from cipher_utils import *

def atbash_encode(s):
    ret = ''
    l = list(s)
    
    for i in l:
        if (re.search("[a-zA-Z]",i)):
            ret += num_to_letter(25-letter_to_num(i))
        else:
            ret += i
    return ret