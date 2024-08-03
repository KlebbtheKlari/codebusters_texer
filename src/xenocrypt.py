######
# Xenocrypt!
# including K1, K2, K3
# Frequency tables available as a util
######

import random
import re
from cipher_utils import *

alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

class Xenocrypt:
    
    # note: variable k is an integer in [1,2,3] for K-k alphabet
    def __init__(self, plaintext,value,type,key=None,shift=None,k=None):
        self.pt = plaintext.upper()
        self.val = int(value)
        self.type = answerize(type)
        
        if (k == None):
            self.ct = self.random_aristo(plaintext)
        else:
            self.k = int(k)
            self.key = key.upper()
            self.shift = int(shift)
            k_alph = self.gen_k_alphabet(self.key,self.shift)
            if (k == 1):
                self.ct = self.aristo_encoder(self.pt,k_alph,alphabet)
            elif (k == 2):
                self.ct = self.aristo_encoder(self.pt,alphabet,k_alph)
            elif (k==3):
                alph = self.gen_k_alphabet(self.key,0)
                self.ct = self.aristo_encoder(self.pt,k_alph,alph)


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
    

    # generate K alphabet with key & shift
    def gen_k_alphabet(self,key,shift):
        # method to circular shift string fwd by n
        def circle_shift(s):
            ns = ''
            for i in range(-shift,-shift+27):
                ns += s[i%27]
            return ns
        
        s = key
        for i in list(alphabet):
            if (i not in list(s)):
                s += i
        s = circle_shift(s)
        return s


    # transforms s to ciphertext using pt-ct alphabet mapping
    def aristo_encoder(self,s, pt_alphabet, ct_alphabet):
        mapping = {}
        pt = list(pt_alphabet)
        ct = list(ct_alphabet)
        ret = ''
        for i in range(len(pt)):
            mapping[pt[i]] = ct[i]
        print(mapping)
        
        l = list(s)
        for i in l:
            if (re.search("[a-zA-ZñÑáéíóúÁÉÍÓÚ]",i)):
                i = i.upper()
                ret += mapping[i]
            else:
                ret += i
        return ret


    def random_aristo(self,s):
        ct_alph = self.gen_random_alphabet()
        return self.aristo_encoder(s,alphabet,ct_alph)

# a = Xenocrypt("Do not dwell upon those",1,"type","plot")
# print(a.ct)