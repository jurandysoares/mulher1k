#!/usr/bin/python3
import os

for n in os.listdir():
    num,nome = n.split('-')
    os.rename(n, '-'.join((num, nome[::-1])))

    

    
