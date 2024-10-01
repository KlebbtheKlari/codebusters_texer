######
# Porta!
######

from cipher_utils import *
from math import floor

class Porta:
    # string pt, string ct, int val, string key, string type, bool bonus
    
    def __init__(self, type,val,plaintext,key,bonus,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.key = answerize(key)
        self.bonus = bonus
        self.has_crib = False
        
        if (crib == None):
            self.ct = blockify(self.porta_encode(self.pt,self.key),len(self.key))
        else:
            self.crib = answerize(crib)
            self.has_crib = True
            self.ct = blockify(self.porta_encode(self.pt,self.key),5)
            self.ct_crib = answerize(self.porta_encode(self.crib,self.key))
    
    
    def porta_encode(self,pt,key):
        l = len(key)
        ret = ''
        
        for i in range(len(pt)):
            n = letter_to_num(pt[i])
            if (n < 13):
                ret += A0Z25( (n + floor(letter_to_num(key[i%l])/2) %13) + 13 )
            else:
                ret += A0Z25( (n - floor(letter_to_num(key[i%l])/2) %13) + 13 )
        return ret
    
    
    # TODO: return the entire texed version
    # TODO: Add the position of crib
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Porta}} cipher'.format(42)
        
        # TODO: if a crib exists, add it
        if (self.has_crib):
            ret += '. The [numbers] ciphertext letters '
            ret += str(self.ct_crib)
            ret += ' decode to the plaintext '
            ret += str(self.crib)
            ret += '. Note that the while the ciphertext is in blocks of 5 letters,'
            ret += ' the key may not be 5 letters long'
            
        # if no crib exists, give the key
        else:
            ret += ' with the key \\textbf{{'.format(42)
            ret += self.key
            ret += '}}'.format(42)
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