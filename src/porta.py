######
# Porta!
######

from cipher_utils import *
from math import floor

class Porta:
    # string pt, string ct, int val, string key, string type, bool bonus
    
    def __init__(self, type,val,plaintext,key,bonus,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.key = answerize(key)
        self.bonus = bonus
        
        if (crib == None):
            self.ct = blockify(self.porta_encode(self.pt,self.key),len(self.key))
        else:
            self.crib = answerize(crib)
            self.ct = blockify(self.porta_encode(self.pt,self.key),5)
            x = answerize(self.ct)
            # print(x)
            self.ct_crib = x[(len(x) - len(self.crib)):]
            # print(self.ct_crib)
    
    
    def porta_encode(self,pt,key):
        l = len(key)
        ret = ''
        
        for i in range(len(pt)):
            n = letter_to_num(pt[i])
            if (n < 13):
                ret += A0Z25( ((n + floor(letter_to_num(key[i%l])/2)) %13) + 13 )
            else:
                ret += A0Z25( (n - floor(letter_to_num(key[i%l])/2)) %13 )
        return ret
    
    
    # TODO: Add the position of crib
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Porta}} cipher'.format(42)
        
        # TODO: if a crib exists, add it
        if (self.type == 'CRIB'):
            ret += '. The [numbers] ciphertext letters '
            ret += str(self.ct_crib)
            ret += ' decode to the plaintext '
            ret += str(self.crib)
            ret += '. Note that the while the ciphertext is in blocks of 5 letters,'
            ret += ' the key may not be 5 letters long'
            
        # if no crib exists, give the key
        else:
            ret += ' with the key \\textbf{{'.format(42)
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
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret

# p = Porta('type',1,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','BISW',False)
# print(p.ct)