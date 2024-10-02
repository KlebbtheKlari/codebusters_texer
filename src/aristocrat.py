######
# Aristocrats
# including K1, K2, K3
# Frequency tables available as a util
######

import random
import re
from cipher_utils import *

class Aristocrat:
    
    # note: variable k is an integer in [1,2,3] for K-k alphabet
    def __init__(self, plaintext,value,type,key=None,shift=None,k=None):
        self.pt = plaintext.upper()
        self.val = int(value)
        self.type = type.upper()
        
        if (k == None):
            self.ct = self.random_aristo(plaintext)
            self.k = 0
        else:
            self.k = int(k)
            self.key = answerize(key)
            self.shift = int(shift)
            k_alph = gen_k_alphabet(strip_repeats(self.key),self.shift)
            if (self.k == 1):
                self.ct = self.aristo_encoder(self.pt,k_alph,alphabet)
            elif (self.k == 2):
                self.ct = self.aristo_encoder(self.pt,alphabet,k_alph)
            elif (self.k == 3):
                alph = gen_k_alphabet(self.key,0)
                self.ct = self.aristo_encoder(self.pt,k_alph,alph)

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
    
    # TODO: return the entire texed version
    def __str__(self):
        ret = ''
        
        # question statement
        if (self.type == 'DECODE'):
            ret += '\\question['
            ret += str(self.val)
            ret += '] Solve this \\textbf{{Aristocrat}}'.format(42)
            if (self.k > 0):
                ret += ' that was encoded using a K'
                ret += str(self.k)
                ret += ' alphabet'
            ret += '.'
        else:
            ret += '\\question['
            ret += str(self.val)
            ret += '] This \\textbf{{Aristocrat}} was encoded using a K'.format(42)
            ret += str(self.k)
            ret += ' alphabet '
            ret += ' with a key \\todo{{Add key enumerations}}.'.format(42)
            ret += ' What key was used?'
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        # freq table
        ret += '\n'
        
        ret += '\\begin{{tabular}}{{|m{{2cm}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|}}'.format(42)
        ret += '\n'
        ret += '\\hline'
        ret += '\n'
        
        o = ''''''
        for i in range(26):
            o += '&'
            o += chr(i+65)
        o += '\\\\'
        o += '\n'
        o += '\\hline'
        o += '\n'
        o += 'Frequency'
        for i in range(26):
            o += '&'
            o += str(self.ct.count(chr(i+65)))
        o += '\\\\'
        o += '\n'
        o += '\\hline'
        o += '\n'
        o += 'Replacement'
        for i in range(26):
            o += '&'
        
        ret += o
        ret += '\\\\'
        ret += '\n'
        
        ret += '\\hline'
        ret += '\n'
        ret += '\\end{{tabular}}'.format(42)
        
        return ret

# a = Aristocrat("Do not dwell upon those",5,"type","keyeee",4,1)
# print(a)