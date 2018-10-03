#-*- coding: utf-8 -*- 
import sys
import hashlib
def _SHA1_(str1):				
	print('SHA1 encoding...')
	print('Результат: '+hashlib.sha1(str1.encode('utf-8')).hexdigest())
def _SHA224_(str1):    
    print('SHA224 encoding...')
    print('Результат: '+hashlib.sha224(str1.encode('utf-8')).hexdigest())
def _SHA256_(str1):
	print('SHA256 encoding...')
	print('Результат: '+hashlib.sha256(str1.encode('utf-8')).hexdigest())
def _SHA384_(str1):
	print('SHA384 encoding...')
	print('Результат: '+hashlib.sha384(str1.encode('utf-8')).hexdigest())
def _SHA512_(str1):
	print('SHA512 encoding...')
	print('Результат: '+hashlib.sha512(str1.encode('utf-8')).hexdigest())
def _MD5_encode(str1):
	print('md5 encoding...')
	print('Результат: '+hashlib.md5(str1.encode('utf-8')).hexdigest())

