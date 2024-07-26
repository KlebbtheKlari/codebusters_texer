######
# Aristocrats
# including K1, K2, K3
# Frequency tables available as a util
######

import random
import re

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Monoalphabetic:
    def __init__(self, plaintext,value,cipher,type,alphabet=None):
        self.pt = plaintext
        self.val = value
        self.type = type
        
        if (alphabet == None):
            self.alphabet = ""
        else:
            self.alphabet = alphabet
        # Generate pt-ct mapping
        # Encode (& parse if pat), store ct


# generates a random alphabet
# ensures that no letter is in the same position
# as in the normal alphabet
def gen_random_alphabet():
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

# transforms s to ciphertext
def aristo_encoder(s, pt_alphabet, ct_alphabet):
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

def random_aristo(s):
    ct = gen_random_alphabet()
    return aristo_encoder(s,alphabet,ct)
