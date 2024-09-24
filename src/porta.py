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
        
        if (crib == None):
            self.ct = blockify(self.porta_encode(self.pt,self.key),len(self.key))
        else:
            self.crib = answerize(crib)
            self.ct = blockify(self.porta_encode(self.pt,self.key),5)
    
    
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
    def __str__(self):
        return self.ct