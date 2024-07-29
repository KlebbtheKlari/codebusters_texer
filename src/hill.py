from cipher_utils import *
from math import sqrt

class Hill:
    def __init__(self, plaintext,value,key,bonus):
        self.pt = plaintext.upper()
        self.key = key.upper()
        self.size = int(sqrt(len(self.key)))
        # pad pt so it's a multiple of size
        while (len(self.pt) % self.size != 0):
            self.pt += 'Z'
        
        self.val = value
        self.encmatrix = self.key_to_matrix()
        self.ct = self.hill_encode()
        self.bonus = bonus
        
        if (self.size > 4):
            self.decmatrix = self.invert()
    
    
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