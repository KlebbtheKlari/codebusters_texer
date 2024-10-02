######
# Baconian!
######

from cipher_utils import *

class Baconian:
    
    def __init__(self, type,val,plaintext,bonus,amt=None,crib=None):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = answerize(plaintext)
        self.bin = self.baconian_encode(self.pt)
        self.bonus = bonus # bool
        if (crib == None):
            pass
        else:
            self.crib = answerize(crib)

        # amt == number of chars to a/b
        # by default, self.amt == 1
        # for word bacon, amt == block size
        # and if amt == 1, mapping is random
        # (thus ABABABAB... is impossible)
        if (amt == None):
            self.amt = 1
        else:
            self.amt = int(amt)
            
        if (self.type == "DECODE"):
            self.ct = self.baconian_letters(self.bin,self.amt)
        elif (self.type == "SEQUENCE"):
            self.ct = 'seq'
        else:
            self.ct = 'word'
            
        
    def baconian_encode(self,pt):
        ret = ''
        
        # cipher-utils.baconify()
        # converts to binary, NOT A/B
        for i in pt:
            ret += baconify(i)
        
        return ret
    
    # converts BINARY STRING to letter bacon ciphertext
    # with amt letters as A and amt as B
    # by default, the order of letters are random
    # so A letters don't repeat regularly, neither do Bs
    def baconian_letters(self,ct,amt):
        
        # generate the letters for A's/B's
        a = gen_random_alphabet()
        a_lets = []
        b_lets = []
        for i in range(amt):
            a_lets.append(a[i])
            b_lets.append(a[amt+i])
        
        ret = ''
        for i in ct:
            if i=='0':
                ret += a_lets[random.randint(0,amt-1)]
            else:
                ret += b_lets[random.randint(0,amt-1)]
        return ret
    
    
    # TODO: words, sequence
    # only letter implemented for now
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Baconian}} cipher'.format(42)
        
        # TODO: if a crib exists, add it
        
        ret += '.'
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2.5}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        ret += blockify(self.ct,45)
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret
    
f = Baconian('decode',1,"XLB is tastyasoidjhoaidhgoiuadhg",False,2,'crib')
print(f)