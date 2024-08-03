######
# Fractionated Morse!
######

from aristocrat import gen_k_alphabet
from cipher_utils import *

class Fracmorse:
    
    def __init__(self, type,val,plaintext,key,bonus,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = plaintext.upper()
        self.key = answerize(key)
        
    def fracmorse_encode(self,pt,key):
        alphabet = gen_k_alphabet(key)
        pass