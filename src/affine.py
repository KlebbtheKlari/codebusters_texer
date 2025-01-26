######
# Affine cipher!
######

import re
from cipher_utils import *

class Affine:
    # string pt, string ct, int val, tuple (int,int) key
    
    def __init__(self, type, plaintext, value, keyA, keyB, bonus, crib=None):
        self.type = type
        self.pt = answerize(plaintext)
        self.val = value
        self.key = (int(keyA), int(keyB))
        self.ct = blockify(self.affine_encode(self.pt, self.key[0], self.key[1]),5)
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
    
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Affine}} cipher'.format(42)
        
        if (self.type == 'CRIB'):
            ret += '. '
            ret += 'The ciphertext letters \\textbf{{'.format(42)
            ret += self.affine_encode(self.crib,self.key[0],self.key[1])
            ret += '}} decode to the plaintext letters \\textbf{{'.format(42)
            ret += self.crib
            ret += '}}.'
        # if no crib exists, give the key
        else:
            ret += ' with the key $(A,B) = ('.format(42)
            ret += str(self.key[0])
            ret += ','.format(42)
            ret += str(self.key[1])
            ret += ')$'
            ret += '.'
        
        # if bonus, say so.
        if (self.bonus):
            ret += '\n'
            ret += '\\emph{{$\\bigstar$\\textbf{{This question is a special bonus question.}} }}'.format(42)
        
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

# a = Affine('type','a.',12,'7','3',False)
# print(a)