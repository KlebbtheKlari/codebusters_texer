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
            self.ct = self.random_aristo(self.pt)
            self.k = 0
        else:
            self.k = int(k)
            self.key = key.upper()
            self.shift = int(shift)
            k_alph = self.gen_k_alphabet(strip_repeats(self.key),self.shift)
            if (self.k == 1):
                self.ct = self.aristo_encoder(self.pt,k_alph,alphabet)
            elif (self.k == 2):
                self.ct = self.aristo_encoder(self.pt,alphabet,k_alph)
            elif (self.k==3):
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
        # print(mapping)
        
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
    
    
    # TODO: return the entire texed version
    def __str__(self):
        ret = ''
        
        # question statement
        if (self.type == 'DECODE'):
            ret += '\\question['
            ret += str(self.val)
            ret += '] Solve this \\textbf{{Spanish Aristocrat}}'.format(42)
            if (self.k > 0):
                ret += ' that was encoded using a K'
                ret += str(self.k)
                ret += ' alphabet'
            ret += '.'
        else:
            ret += '\\question['
            ret += str(self.val)
            ret += '] This \\textbf{{Spanish Aristocrat}} was encoded using a K'.format(42)
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
        
        if (self.k != 2):
            o = ''''''
            for i in range(27):
                o += '&'
                if (i < 14):
                    o += chr(i+65)
                elif (i >= 15):
                    o += chr(i+64)
                else:
                    o += chr(209)
            o += '\\\\'
            o += '\n'
            o += '\\hline'
            o += '\n'
            o += 'Frequency'
            for i in range(27):
                o += '&'
                if (i < 14):
                    o += str(self.ct.count(chr(i+65)))
                elif (i > 15):
                    o += str(self.ct.count(chr(i+65-1)))
                else:
                    o += str(self.ct.count(chr(209)))
            o += '\\\\'
            o += '\n'
            o += '\\hline'
            o += '\n'
            o += 'Replacement'
            for i in range(27):
                o += '&'
            
            ret += o
            ret += '\\\\'
            ret += '\n'
            
            ret += '\\hline'
            ret += '\n'
            ret += '\\end{{tabular}}'.format(42)
            
        # k2 has replacement first
        else:
            o = ''''''
            o += 'Replacement'
            for i in range(27):
                o += '&'
            o += '\\\\'
            o += '\n'
            o += '\\hline'
            o += '\n'
            o += 'K2'
            for i in range(27):
                o += '&'
                if (i < 14):
                    o += chr(i+65)
                elif (i >= 15):
                    o += chr(i+64)
                else:
                    o += chr(209)
            o += '\\\\'
            o += '\n'
            o += '\\hline'
            o += '\n'
            o += 'Frequency'
            for i in range(27):
                o += '&'
                if (i < 14):
                    o += str(self.ct.count(chr(i+65)))
                elif (i > 15):
                    o += str(self.ct.count(chr(i+65-1)))
                else:
                    o += str(self.ct.count(chr(209)))
            
            ret += o
            ret += '\\\\'
            ret += '\n'
            
            ret += '\\hline'
            ret += '\n'
            ret += '\\end{{tabular}}'.format(42)
        
        return ret

# a = Xenocrypt('this is a sample plaintext',100,'type','key',4,2)
# print(a)