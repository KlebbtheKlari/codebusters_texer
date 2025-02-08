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
            self.ct = 'sequence'
        else:
            self.ct = self.baconian_words(self.pt,self.amt)
            
        
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
    
    
    # given lists of which letters
    # are zeroes and which are ones,
    # 
    def build_wordlist(self,zeroes,ones):
        ret = {}
        words = [answerize(word) for word in open('src/words.txt')]
        
        for let in alphabet:
            if let != 'I' and let != 'U':
                ret[let] = []
        
        for word in words:
            bin = ''
            # convert word to baconian via 0/1
            for i in word:
                if i in zeroes:
                    bin += '0'
                else:
                    bin += '1'
            a = sum(pow(2,4-i)*int(bin[i]) for i in range(len(bin)))
            if a >= 24:
                continue
            # print(word,bin)
            
            # de-baconify bin
            ret[debaconify(bin)].append(word)
        # print(ret['A'])
        
        return ret
    
    
    # encodes plaintext directly to words
    def baconian_words(self,pt,amt):
        ret = ''
        
        # build the alphabet
        zeroes = []
        ones = []
        if (amt > 1):
            idx = 0
            c = 0
            start = random.randint(0,1)
            while idx < 26:
                c += 1
                if start == 0:
                    zeroes.append(alphabet[idx])
                else:
                    ones.append(alphabet[idx])
                if c >= amt:
                    start = not start
                    c = 0
                idx += 1
        else:
            alph = gen_random_alphabet()
            zeroes = list(alph[:13])
            ones = list(alph[13:])
        
        # categorize each word in words.txt
        wordlist = self.build_wordlist(zeroes,ones)
        # print(''.join(zeroes))
        # print(''.join(ones))
        
        # match each letter to a random word
        for i in pt:
            let = i
            if i == 'I':
                let = 'J'
            if i == 'U':
                let = 'V'
            r = random.randint(1,len(wordlist[let])-1)
            ret += wordlist[let][r]
            ret += ' '
        
        if len(answerize(ret)) != 5*len(pt):
            print(len(answerize(ret)),"bad")
        
        return ret
    
    
    # TODO: sequence
    def __str__(self):
        ret = ''
        
        # question statement
        ret += '\\question['
        ret += str(self.val)
        ret += '] Decode this sentence that was encoded using the \\textbf{{Baconian}} cipher'.format(42)
        
        # TODO: if a crib exists, add it
        
        ret += '.'
        # if bonus, say so.
        if (self.bonus):
            ret += '\n'
            ret += '\\emph{{$\\bigstar$\\textbf{{This question is a special bonus question.}} }}'.format(42)
        
        ret += '\n'
        ret += '\n'
        
        # ciphertext
        ret += '{{\\setstretch{{2.5}}'.format(42)
        ret += '\n'
        ret += '\\begin{{lstlisting}}[breakindent=0pt,breaklines]'.format(42)
        ret += '\n'
        if (self.type == 'WORDS'):
            ret += self.ct
        else:
            ret += blockify(self.ct,45)
        ret += '\n'
        ret += '\\end{{lstlisting}}'.format(42)
        ret += '\n'
        ret += '}'
        
        return ret
    
# f = Baconian('words',1,"",True,1,'crib')
# print(f)