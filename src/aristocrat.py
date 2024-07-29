######
# Aristocrats
# including K1, K2, K3
# Frequency tables available as a util
######

import random
import re

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Aristocrat:
    
    # note: variable k is an integer in [1,2,3] for K-k alphabet
    def __init__(self, plaintext,value,type,key=None,shift=None,k=None):
        self.pt = plaintext.upper()
        self.val = value
        self.type = type
        
        if (k == None):
            self.alphabet = ""
            self.ct = self.random_aristo(plaintext)
        else:
            self.k = k
            self.key = key
            self.shift = shift
        # Generate pt-ct mapping
        # Encode (& parse if pat), store ct


    # generates a random alphabet
    # ensures that no letter is in the same position
    # as in the normal alphabet
    def gen_random_alphabet(self):
        l = list(alphabet)
        alpha = list(alphabet)
        fixed = False
        
        while(not fixed):
            fixed = True
            random.shuffle(alpha)
            for i in range(len(alpha)):
                if alpha[i] == l[i]:
                    fixed = False
        
        return ''.join(alpha)
    

    # generate K-k alphabet with key & shift
    def gen_k_alphabet(self,k,key,shift):
        return


    # transforms s to ciphertext using pt-ct alphabet mapping
    def aristo_encoder(self,s, pt_alphabet, ct_alphabet):
        mapping = {}
        pt = list(pt_alphabet)
        ct = list(ct_alphabet)
        ret = ''
        for i in range(len(pt)):
            mapping[pt[i]] = ct[i]
        
        l = list(s)
        for i in l:
            if (re.search("[a-zA-Z]",i)):
                i = i.upper()
                ret += mapping[i]
            else:
                ret += i
        return ret


    def random_aristo(self,s):
        ct = self.gen_random_alphabet()
        return self.aristo_encoder(s,alphabet,ct)

a = Aristocrat("abc",1,"type")
print(a.ct)