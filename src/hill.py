from cipher_utils import *
from math import sqrt

class Hill:
    def __init__(self, plaintext,value,key,bonus):
        self.pt = answerize(plaintext)
        self.key = key.upper()
        self.size = int(sqrt(len(self.key)))
        # pad pt so it's a multiple of size
        while (len(self.pt) % self.size != 0):
            self.pt += 'Z'
        
        self.val = value
        self.encmatrix = self.key_to_matrix()
        self.ct = self.hill_encode()
        self.bonus = bonus
        
        if (self.size > 2):
            self.decmatrix = self.invert()
            self.deckey = ''
            for i in self.decmatrix:
                for j in i:
                    self.deckey += A0Z25(j)
    
    
    def key_to_matrix(self):
        mat = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(letter_to_num(self.key[self.size*i+j]))
            mat.append(row)
        return mat
    
    # note: only 3x3 inverse needs to be provided
    # 2x2 inverse is easy to do directly anyway
    def invert(self):
        m = self.encmatrix
        d1 = m[1][1] * m[2][2] - m[2][1] * m[1][2]
        d2 = m[1][0] * m[2][2] - m[1][2] * m[2][0]
        d3 = m[1][0] * m[2][1] - m[1][1] * m[2][0]
        det = (m[0][0] * d1 - m[0][1] * d2 + m[0][2] * d3)%26
        inv = mod_inverse(det,26)
        
        ret = [[0,0,0],[0,0,0],[0,0,0]]
        ret[0][0] = (inv*d1) %26
        ret[0][1] = (inv* (m[0][2] * m[2][1] - m[0][1] * m[2][2])) %26
        ret[0][2] = (inv* (m[0][1] * m[1][2] - m[0][2] * m[1][1])) %26
        ret[1][0] = (inv* (m[1][2] * m[2][0] - m[1][0] * m[2][2])) %26
        ret[1][1] = (inv* (m[0][0] * m[2][2] - m[0][2] * m[2][0])) %26
        ret[1][2] = (inv* (m[1][0] * m[0][2] - m[0][0] * m[1][2])) %26
        ret[2][0] = (inv* d3) %26
        ret[2][1] = (inv* (m[2][0] * m[0][1] - m[0][0] * m[2][1])) %26
        ret[2][2] = (inv* (m[0][0] * m[1][1] - m[1][0] * m[0][1])) %26
        
        return ret
    
    
    def hill_encode(self):
        m = self.encmatrix
        ret = ''
        for i in range(0,len(self.pt),self.size):
            u = [letter_to_num(self.pt[i+k]) for k in range(0,self.size)]
            v = ''
            for j in range(self.size):
                x = 0
                for k in range(self.size):
                    x += m[j][k] * u[k]
                v += num_to_letter(x%26)
            ret += v
        return ret
    
    
    # TODO: return the entire texed version
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Hill}} cipher'.format(42)
            
        # give the key
        ret += ' with the key \\textbf{{'.format(42)
        ret += self.key
        ret += '}}'.format(42)
        ret += '.'
        
        # if bonus, say so.
        if (self.bonus):
            ret += '\n'
            ret += '\\emph{{$\\bigstar$\\textbf{{This question is a special bonus question.}} }}'.format(42)
        
        # add encoding matrix
        ret += '\n'
        ret += '\\['
        ret += '\n'
        ret += '\\begin{{pmatrix}}'.format(42)
        for i in range(len(self.key)):
            ret += self.key[i]
            if ((i+1)% self.size == 0 and i < self.size*self.size -1):
                ret += '\\\\'
            elif (i == self.size*self.size-1):
                break
            else:
                ret += '&'
        ret += '\\end{{pmatrix}} = '.format(42)
        
        ret += '\\begin{{pmatrix}}'.format(42)
        for i in range(len(self.key)):
            ret += str(letter_to_num(self.key[i]))
            if ((i+1)% self.size == 0 and i < self.size*self.size -1):
                ret += '\\\\'
            elif (i == self.size*self.size-1):
                break
            else:
                ret += '&'
        ret += '\\end{{pmatrix}}'.format(42)
        
        # if 3x3, add decoding matrix.
        if (len(self.key) == 9):
            ret += '\\quad '
            ret += '\\quad'
            ret += '\\begin{{pmatrix}}'.format(42)
            for i in range(len(self.key)):
                ret += str(letter_to_num(self.key[i]))
                if ((i+1)% self.size == 0 and i < self.size*self.size -1):
                    ret += '\\\\'
                elif (i == self.size*self.size-1):
                    break
                else:
                    ret += '&'
            ret += '\\end{{pmatrix}}^{{-1}} = '.format(42)
            
            ret += '\\begin{{pmatrix}}'.format(42)
            for i in range(len(self.key)):
                ret += str(letter_to_num(self.deckey[i]))
                if ((i+1)% self.size == 0 and i < self.size*self.size -1):
                    ret += '\\\\'
                elif (i == self.size*self.size-1):
                    break
                else:
                    ret += '&'
            ret += '\\end{{pmatrix}}'.format(42)
        
        ret += '\n'
        ret += '\\]'
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
    
# h = Hill('blah',128,'keyd',False)
# print(h.pt)