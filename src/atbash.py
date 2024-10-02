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
    
    # TODO: return the entire texed version
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Atbash}} cipher'.format(42)
        ret += '.'
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret