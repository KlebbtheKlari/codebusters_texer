from cipher_utils import *

class Hill:
    def __init__(self, plaintext,value,key):
        self.pt = plaintext
        self.val = value
        self.key = key
        