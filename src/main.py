import csv
import codecs

from cipher_utils import *

import affine
import aristocrat
import atbash
import baconian
import caesar
import columnar
import fracmorse
import hill
import nihilist
import patristocrat
import porta
import xenocrypt

filename = 'src/main.csv'

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        

out_filename = 'out.tex'
open(out_filename,"w").close()
out_file = codecs.open(out_filename,'w','utf-8')

count = 0
for row in rows:
    
    cipher = answerize(row[1])
    type = answerize(row[2])
    value = int(row[5])
    bonus = (row[6] == 'TRUE')
    pt = row[7]
    key1 = row[9]
    key2 = row[10]
    key3 = row[11]
    
    question = ''
    
    if (cipher == 'ARISTOCRAT'):
        # IF a k-key exists, form a k alphabet
        if (key1 != ''):
            question = aristocrat.Aristocrat(pt,value,type,answerize(key1),key2,key3)
        else:
            question = aristocrat.Aristocrat(pt,value,type)
        
    elif (cipher == 'PATRISTOCRAT'):
        # IF a k-key exists, form a k alphabet
        if (key1 != ''):
            question = patristocrat.Patristocrat(pt,value,type,answerize(key1),key2,key3)
        else:
            question = patristocrat.Patristocrat(pt,value,type)
            
    elif (cipher == 'XENOCRYPT'):
        # IF a k-key exists, form a k alphabet
        if (key1 != ''):
            question = xenocrypt.Xenocrypt(pt,value,type,answerize(key1),key2,key3)
        else:
            question = xenocrypt.Xenocrypt(pt,value,type)
            
    elif (cipher == 'BACONIAN'):
        if (key1 != '' and key2 != ''):
            question = baconian.Baconian(type,value,pt,bonus,key1,key2)
        elif (key1 != '' and key2 == ''):
            question = baconian.Baconian(type,value,pt,bonus,key1)
        elif (key1 == '' and key2 != ''):
            question = baconian.Baconian(type,value,pt,bonus,None,key2)
        else:
            baconian.Baconian(type,value,pt,bonus)
            
    elif (cipher == 'FRACMORSE'):
        question = fracmorse.Fracmorse(type,value,pt,key1,bonus,key2)
    
    elif (cipher == 'PORTA'):
        if (key2 != ''):
            question = porta.Porta(type,value,pt,key1,bonus,key2)
        else:
            question = porta.Porta(type,value,pt,key1,bonus)
    
    # elif (cipher == 'COLUMNAR'):
    #     pass
    # elif (cipher == 'NIHILIST'):
    #     pass
    
    elif (cipher == 'HILL'):
        question = hill.Hill(pt,value,key1,bonus)
        
    elif (cipher == 'ATBASH'):
        question = atbash.Atbash(pt,value)
        
    elif (cipher == 'AFFINE'):
        if (key3 != ''):
            question = affine.Affine(type,pt,value,key1,key2,bonus,key3)
        else:
            question = affine.Affine(type,pt,value,key1,key2,bonus)
            
    elif (cipher == 'CAESAR'):
        if (key1 != ''):
            question = caesar.Caesar(pt,value,key1)
        else:
            question = caesar.Caesar(pt,value)
    
    else:
        # add a TODO to typeset manually
        question = '\n' + 'TODO' + '\n'
    
    out_file.write(question.__str__())
    out_file.write('\n')
    out_file.write('\\vfill')
    out_file.write('\n')
    out_file.write('\\uplevel{{\\hrulefill}}'.format(42))
    out_file.write('\n')
    
    if (count%2 == 0):
        out_file.write('\\newpage')
    count += 1