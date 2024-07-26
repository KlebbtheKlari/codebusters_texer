import csv

import cipher_utils

import affine
import atbash
import caesar
import hill
import monoalphabetic

filename = ''

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)