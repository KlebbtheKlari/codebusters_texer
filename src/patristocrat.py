######
# Patristocrats
# including K1, K2, K3
# Frequency tables available as a util
######

import random
import re
from cipher_utils import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Patristocrat:
    
    # note: variable k is an integer in [1,2,3] for K-k alphabet
    def __init__(self, plaintext,value,type,key=None,shift=None,k=None):
        self.pt = answerize(plaintext)
        self.val = int(value)
        self.type = answerize(type)
        
        if (k == None):
            self.ct = self.random_aristo(plaintext)
        else:
            self.k = int(k)
            self.key = key.upper()
            self.shift = int(shift)
            k_alph = gen_k_alphabet(self.key,self.shift)
            if (k == 1):
                self.ct = self.aristo_encoder(self.pt,k_alph,alphabet)
            elif (k == 2):
                self.ct = self.aristo_encoder(self.pt,alphabet,k_alph)
            elif (k==3):
                alph = gen_k_alphabet(self.key,0)
                self.ct = self.aristo_encoder(self.pt,k_alph,alph)
        self.ct = blockify(self.ct,5)


    # transforms s to ciphertext using pt-ct alphabet mapping
    def aristo_encoder(self,s, pt_alphabet, ct_alphabet):
        mapping = {}
        pt = list(pt_alphabet)
        ct = list(ct_alphabet)
        ret = ''
        for i in range(len(pt)):
            mapping[pt[i]] = ct[i]
        # print(mapping)
        
        l = list(s)
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += mapping[i]
            else:
                ret += i
        return ret


    def random_aristo(self,s):
        ct_alph = gen_random_alphabet()
        return self.aristo_encoder(s,alphabet,ct_alph)

# a = Patristocrat("These",1,"type","plot",2,3)
# print(a.ct)