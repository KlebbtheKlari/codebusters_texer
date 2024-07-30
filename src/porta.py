######
# Porta!
######

from cipher_utils import *

class Porta:
    # string pt, string ct, int val, string key, string type, bool bonus
    
    def __init__(self, type,val,plaintext,key,bonus,crib=None):
        self.type = type
        self.val = val
        self.pt = answerize(plaintext)
        self.key = answerize(key)
        self.bonus = bonus
        
        if (crib == None):
            self.ct = blockify(self.porta_encode(self.pt,self.key),len(key))
        else:
            self.crib = crib
            self.ct = blockify(self.porta_encode(self.pt,self.key),5)
    
    
    def porta_encode(self,pt,key):
        return