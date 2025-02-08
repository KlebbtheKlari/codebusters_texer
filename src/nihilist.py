######
# Nihilist!
######

from cipher_utils import *
from math import floor

class Nihilist:
    # string pt, string ct, int val, string key, string type, bool bonus
    
    def __init__(self, type,val,plaintext,bonus,poly,key,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.poly = answerize(poly)
        self.key = answerize(key)
        self.bonus = bonus
        self.ct = self.nihilist_encode(self.pt,self.poly,self.key)
        
        if (crib == None):
            pass
        else:
            self.crib = answerize(crib)
            self.crib_start = self.pt.find(self.crib)
            self.ct_crib = ' '.join(self.ct[self.crib_start:self.crib_start + len(self.crib)])
    
    def nihilist_encode(self,pt,poly,key):
        ret = []
        
        cts = {}
        poly_alpha = gen_k_alphabet(poly,0)
        poly_alpha = poly_alpha.replace("J","") # combine I/J
        new_pt = pt.replace("J","I")
        idx = 0
        for i in range(1,6):
            for j in range(1,6):
                cts[poly_alpha[idx]] = 10*i + j
                idx += 1
        
        for i in range(len(pt)):
            ret.append(str(cts[new_pt[i]] + cts[key[i%len(key)]]))
        
        return ret
    
    
    # TODO: TABLE
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Nihilist Substitution}} cipher'.format(42)
        
        # TODO: if a crib exists, add it
        if (self.type == 'CRIB'):
            ret += ' using a (non-Polybius) key that was 3 to 7 letters long inclusive'
            ret += '. The '
            ret += ordinal(self.crib_start+1)
            ret += ' to '
            ret += ordinal(self.crib_start + len(self.crib))
            ret += ' ciphertext numbers '
            ret += str(self.ct_crib)
            ret += ' decode to the plaintext letters '
            ret += str(self.crib)
            ret += '.'
            
        # if no crib exists, give the key
        else:
            ret += ' with the Polybius key \\textbf{{'.format(42)
            ret += self.poly
            ret += '}} and the key \\textbf{{'.format(42)
            ret += self.key
            ret += '}}'.format(42)
            ret += '.'
        
        # if bonus, say so.
        if (self.bonus):
            ret += '\n'
            ret += '\\emph{{$\\bigstar$\\textbf{{This question is a special bonus question.}} }}'.format(42)
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        ret += ' '.join(self.ct)
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret
    
# n = Nihilist("DECODE",1,"TEST PLAINTEXT",True,"POLYBIYUS","KEY","TEST")
# print(n)