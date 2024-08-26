######
# Baconian!
######

from cipher_utils import *

class Baconian:
    
    def __init__(self, type,val,plaintext,bonus,amt=None,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.bin = self.baconian_encode(self.pt)
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
            self.ct = self.baconian_letters(self.bin,self.amt)
        elif (self.type == "SEQUENCE"):
            self.ct = 'seq'
        else:
            self.ct = 'word'
            
        
    def baconian_encode(self,pt):
        ret = ''
        
        # cipher-utils.baconify()
        # converts to binary, NOT A/B
        for i in pt:
            ret += baconify(i)
        
        return ret
    
    def baconian_letters(self,ct,amt):
        a = gen_random_alphabet()
        a_lets = []
        b_lets = []
        for i in range(amt):
            a_lets.append(a[i])
            b_lets.append(a[amt+i])
        
        ret = ''
        for i in ct:
            if i=='0':
                ret += a_lets[random.randint(0,amt-1)]
            else:
                ret += b_lets[random.randint(0,amt-1)]
        return ret
    
f = Baconian('letter',1,"XLB is tasty",False,2,'crib')
print(blockify(f.ct,5))