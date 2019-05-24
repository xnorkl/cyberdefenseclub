#!/usr/bin/python

import argparse
import math
import os
from itertools import combinations, permutations, chain, product, repeat

#-----------------------------what it do
# bifrost is brute force tool I wrote for NCL hoping to brute force my way into some binary
# that checked for a flag. NCL flags follow a rubrick so if you need to brute force something
# else, you are better off rolling your own tool. Kinda interested in making this a real tool.
#
# Run bifrost.py [Known String] [Flag Length] [A] [B] [Output]
# As is, just consider this a narrow tool that did simply what I needed it to.
# I might or might not refine this hunk of junk later.


parser = argparse.ArgumentParser(description='May the bifrost guide your way.')
parser.add_argument("string", type=str)
parser.add_argument("length", type=int) 
parser.add_argument("arange", type=int)
parser.add_argument("brange", type=int)
parser.add_argument("output", type=str)
arg = parser.parse_args()

#-------------------------------build
def get_known_list(kstring):
    klist = [i for i in kstring]
    return klist

def build_matrix(klist,l,n,m):
    r = l - len(klist)
    #r = 4
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matrx_int = list(product(range(n,m+1), repeat=r))
    matrx_alph = list(product(sample,repeat=r))
    delm = ['-']
    matrx_alph = [klist + [i] + delm for i in matrx_alph]
    #print(matrx_alph)
    #payload = [klist + [i] for i in matrx_alph]
    # print(payload)
    payload = [list(matrx_alph[i]).append(matrx_int[i]) for i in matrx_alph]
    print(payload)
    return payload 

def build_payload(payload,output):
    file = open(output,"w")
    for i in payload:
        pl = str(i).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","").replace("(","").replace(")","")
        file.write(pl + '\n')
    file.close()
    return

k_list = get_known_list(arg.string)
payload = (build_matrix(k_list,arg.length,arg.arange,arg.brange))

build_payload(payload,arg.output)


