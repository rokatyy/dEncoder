
#-*- coding: utf-8 -*-
import sys
import re
from collections import Counter

def analise():
    print('Ввод')
    str1 = (input()).lower()
    c = Counter(str1)
    max = -1
    boollist = []
    symbol_number = 0
    for i in range(ord('a'),ord('z')+1):
        st = chr(i)    
        boollist.append(c[st])
        if (c[st]>max):
            max = c[st]
            maxindex = i
        #print(bool_list)
        print('Количество вхождений ("' + chr(i)+'") = '+str(c[st]))
        symbol_number=symbol_number+1
def _INFO_():
	f = open('info.txt','r')
	print(f.read())