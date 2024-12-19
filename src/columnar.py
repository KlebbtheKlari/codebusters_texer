######
# Porta!
######

from cipher_utils import *
from math import floor

class Columnar:
    # string pt, string ct, int val, string key, string type, bool bonus
    
    def __init__(self, type,val,plaintext,bonus,crib,cols):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.cols = int(cols)
        self.bonus = bonus
        
        self.crib = answerize(crib)
        self.ct = blockify(self.columnar_encode(self.pt,self.cols),5)
    
    def columnar_encode(self,pt,cols):
        ret = ''
        rows = len(pt)//cols
        nums = [i for i in range(cols)]
        random.shuffle(nums)
        
        for i in range(cols):
            for j in range(rows):
                ret += pt[nums[i]+j*cols]
        return ret
    
    
    # TODO: Move to string
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

p = Columnar('type',1,'ABCDEFGHIJKLMNOPQR',False,'ABC',3)
print(p.ct)