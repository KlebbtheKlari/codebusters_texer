######
# Columnar!
######

from cipher_utils import *
from math import floor

class Columnar:    
    def __init__(self, type,val,plaintext,bonus,crib,cols):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.cols = int(cols)
        while (len(self.pt) % self.cols != 0):
            self.pt += 'X'
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
    
    
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Complete Columnar}} cipher.'.format(42)
        
        # crib
        ret += ' The letters \\textbf{{'.format(42)
        ret += str(self.crib)
        ret += '}} appear in the plaintext.'.format(42)
        
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