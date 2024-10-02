######
# Fractionated Morse!
######

from cipher_utils import *

class Fracmorse:
    
    def __init__(self, type,val,plaintext,key,bonus,crib):
        self.type = answerize(type)
        self.val = int(val)
        self.pt = plaintext.upper()
        self.key = answerize(key)
        self.ct = self.fracmorse_encode(self.pt, self.key)
        self.bonus = bonus # bool
        self.crib = answerize(crib)
        
    def fracmorse_encode(self,pt,key):
        ret = '' # string to be returned
        
        alphabet = gen_k_alphabet(key,0) # from aristocrat.py
        morse_string = to_morse(pt) # util
        
        # convert morse -> ternary
        morse_string = morse_string.replace('.','0')
        morse_string = morse_string.replace('-','1')
        morse_string = morse_string.replace('x','2')
        
        morse_string = morse_string[:-1]
        
        # pad extra x's at the end if needed
        while (len(morse_string) % 3 != 0):
            morse_string += '2'
        
        # read chars from alphabet using ternary
        counter = 0
        for i in range(0,len(morse_string),3):
            x = int(morse_string[i])
            y = int(morse_string[i+1])
            z = int(morse_string[i+2])
            ret += alphabet[9*x+3*y+z]
            ret += '  '
            
            # (roughly) breaks by words
            # could be improved in the future, maybe.
            if (i >= 3):
                l = [str(x)+str(y)]
                l.append(str(y)+str(z))
                l.append(morse_string[i-1]+str(x))
                l.append(morse_string[i-2]+morse_string[i-1])
                if (l.count('22') >= 1 and counter > 12):
                    ret += '\n'
                    counter = 0
            counter += 1
        
        return ret
    
    # TODO: return the entire texed version
    # TODO: crib not at beginning
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Fractionated Morse}} cipher'.format(42)
        
        # add crib
        if (self.type == 'CRIB'):
            ret += '. The plaintext begins with the letters \\textbf{{'.format(42)
            ret += str(self.crib)
            ret += '}}'.format(42)
        ret += '.'
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2.5}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        # TODO: fracmorse table
        ret += '\n'
        ret += '\\begin{{center}}'.format(42)
        ret += '\n'
        
        ret += '\\begin{{tabular}}{{|m{{2cm}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|'.format(42)
        ret += 'm{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|m{{9.675pt}}|}}'.format(42)
        
        ret += '\n'
        ret += '\\hline'
        ret += '\n'
        ret += 'Replacement&&&&&&&&&&&&&&&&&&&&&&&&&&\\\\'
        ret += '\n'
        ret += '\\hline'
        ret += '\n'
        
        ret += '&$\\newmoon$&$\\newmoon$&$\\newmoon$&$\\newmoon$&$\\newmoon$&$\\newmoon$&$\\newmoon$&'.format(42)
        ret += '$\\newmoon$&$\\newmoon$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$\\times$&$\\times$&$\\times$&'.format(42)
        ret += '$\\times$&$\\times$&$\\times$&$\\times$&$\\times$\\\\'.format(42)
        ret += '\n'
        
        ret += '&$\\newmoon$&$\\newmoon$&$\\newmoon$&$-$&$-$&$-$&$\\times$&$\\times$&$\\times$&$\\newmoon$&$\\newmoon$&'.format(42)
        ret += '$\\newmoon$&$-$&$-$&$-$&$\\times$&$\\times$&$\\times$&$\\newmoon$&$\\newmoon$&$\\newmoon$&$-$&$-$&$-$&$\\times$&$\\times$\\\\'.format(42)
        ret += '\n'
        
        ret += '&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&'.format(42)
        ret += '$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$&$\\times$&$\\newmoon$&$-$\\\\'.format(42)
        
        ret += '\n'
        ret += '\\hline'
        ret += '\n'
        ret += '\\end{{tabular}}'.format(42)
        ret += '\n'
        ret += '\\end{{center}}'.format(42)
        
        return ret
    
f = Fracmorse('crib',1,'here is a quote at random, i dont know if this works yet','sleight',False,'crib')
print(f)