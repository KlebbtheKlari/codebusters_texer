######
# Baconian!
######

from cipher_utils import *

class Baconian:
    
    def __init__(self, type,val,plaintext,key,bonus,amt=None,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.key = answerize(key)
        self.bin = self.baconian_encode(self.pt, self.key)
        self.bonus = bonus # bool
        if (crib == None):
            pass
        else:
            self.crib = answerize(crib)
        # amt == number of chars to a/b
        # by default, self.amt == 1
        if (amt == None):
            self.amt = 1
        else:
            self.amt = int(amt)
            
        if (self.type == "LETTER"):
            self.ct = self.bin
        elif (self.type == "SEQUENCE"):
            self.ct = 'seq'
        else:
            self.ct = 'word'
            
        
    def baconian_encode(self,pt,key):
        ret = ''
        
        for i in pt:            
            ret += baconify(i)
        
        return ret
    
f = Baconian('letter',1,alphabet,'sleight',False,2,'crib')
print(blockify(f.ct,5))