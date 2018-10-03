#-*- coding: utf-8 -*-
import re
import sys 
import rsa
import hashlib
import base64
import crypto
from cryptography.fernet import Fernet 
from Crypto.PublicKey import RSA
def _base_64(str1):
	str1 = str(base64.b64encode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))
def _base_32(str1):
	str1 = str(base64.b32encode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))	
def _base_16(str1):
	str1 = str(base64.b16encode(bytes(str1, "utf-8")))
	str1 = str1.replace("b'","")
	str1 = str1.replace("'","")
	print('Результат: '+ (str1))
def encode_vizener(m,k):
    k *= len(m) // len(k) + 1
    c = ''.join([chr((ord(j) + ord(k[i])) % 26 + ord('A')) for i, j in enumerate(m)])
    print('Результат: '+c)
def encode_caesar(s):
	alpha = ' abcdefghijklmnopqrstuvwxyz0123456789'	
	s = "".join([z for d in ' '.join(a for a in s.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")
	n = int(input('Введите число сдвига: '))
	s = s.strip().lower()
	res = ''
	for c in s:
		res += alpha[(alpha.index(c) + n) % len(alpha)]
	print('Результат: "' + res + '"')

