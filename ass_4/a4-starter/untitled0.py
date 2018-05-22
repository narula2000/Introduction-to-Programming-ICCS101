# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:14:23 2018

@author: asus
"""
msg="monosodium glutamate"
key=7
x=0
b=""
for y in range(1,len(msg)):
    while len(b)<=key*y-1:
        b=b+msg[x]
        x=x+key
        if x>=len(msg):
            x=y-1
        if x==0:
            x=x+y
    if len(b)==len(msg):
        print(b)
        