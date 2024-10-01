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
        
        # TODO: Strip extra x at end before padding
        
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
            
            l = [x,y,z]
            if (l.count(2) >= 2 and counter > 15):
                ret += '\n'
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
            ret += '. The plaintext begins with the letters '
            ret += str(self.crib)
        ret += '.'
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breaklines]'.format(42)
        ret += '\n'
        ret += self.ct
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        # TODO: fracmorse table
        '''
        \begin{center}
        \begin{tabular}{|m{2cm}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|m{9.675pt}|}
        \hline
        Replacement&&&&&&&&&&&&&&&&&&&&&&&&&&\\
        \hline
        &$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$\newmoon$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$-$&$\times$&$\times$&$\times$&$\times$&$\times$&$\times$&$\times$&$\times$\\
        &$\newmoon$&$\newmoon$&$\newmoon$&$-$&$-$&$-$&$\times$&$\times$&$\times$&$\newmoon$&$\newmoon$&$\newmoon$&$-$&$-$&$-$&$\times$&$\times$&$\times$&$\newmoon$&$\newmoon$&$\newmoon$&$-$&$-$&$-$&$\times$&$\times$\\
        &$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$&$\times$&$\newmoon$&$-$\\
        \hline
        \end{tabular}
        \end{center}
        '''
        
        return ret
    
f = Fracmorse('type',1,'This is a sample sentence','sleight',False,'crib')
print(f.ct)