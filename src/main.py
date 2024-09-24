import csv

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

filename = 'template.csv'

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        

out_filename = 'out.tex'
out_file = open(out_filename,'w')


for row in rows:
    aristocrat.__str__()