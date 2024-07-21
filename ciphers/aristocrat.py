######
# Aristocrats
# including K1, K2, K3, Xeno, Pats
# Frequency tables available as a util
######

import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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


def aristo_encoder(s, pt_alphabet, ct_alphabet):
    mapping = {}
    pt = list(pt_alphabet)
    ct = list(ct_alphabet)
    for i in pt:
        mapping[i] = ct[i]

def random_aristo(s):
    ct = gen_random_alphabet()
    return aristo_encoder(s,alphabet,ct)

