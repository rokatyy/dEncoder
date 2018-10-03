#-*- coding: utf-8 -*-
import base64
import re
import sys
import rsa
from Crypto.PublicKey import RSA
def decode_vizener(c,k):
    k *= len(c) // len(k) + 1 
    m = ''.join([chr((ord(j) - ord(k[i])) % 26 + ord('A')) for i, j in enumerate(c)]) 
    print('Результат: '+m)
def _base_d64code(str1):
	str1 = str(base64.b64decode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))
def _base_d32code(str1):
	str1 = str(base64.b32decode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))	
def _base_d16code(str1):
	str1 = str(base64.b16decode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))
def decode_caesar(s):
	alpha = ' abcdefghijklmnopqrstuvwxyz'
	n = int(input('Введите число сдвига: '))
	s = s.strip() 
	res = ''
	for c in s:
		res += alpha[(alpha.index(c) - n) % len(alpha)]
	print('Результат: "' + res + '"')

