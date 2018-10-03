#-*- coding: utf8 -*-
import sys
import re
import hashlib
from hash import (_SHA1_, _SHA224_,_SHA256_,_SHA384_,_SHA512_,_MD5_encode)
from encoding import (_base_64,_base_32,_base_16,encode_caesar,encode_vizener)
from decoding import (decode_caesar,decode_vizener,_base_d64code,_base_d32code,_base_d16code)
from info import (analise,_INFO_)
from _rsa_ import (encode_rsa, decode_rsa)
def _EXIT_():
	print('Выход..')
	exit(0)
def _return_():
	print('"0" : нажмите для выхода'+'\n'+'"1" : для шифрования'+'\n'+'"2" : для расшифровки'+'\n'+'"3" : для хэширования'+'\n'+'"4" : для частотного анализа'+'\n'+'"5" : для получения информации о шифрах')
	flag=input()	
	if flag  == '1':  Choose_encode()
	elif flag == '0': _EXIT_()
	elif flag == '2': Choose_decode()
	elif flag == '3': Choose_hash()
	elif flag == '4': 
		analise()
		_return_()
	elif flag == '5':
		_INFO_()
		_return_()
	else : 
		print('Ошибка ввода!'+'\n'+'Повторите, пожалуйста:')
		_return_()	
def INPUT():
	global str1
	str1 = input('ВВОД: ')
def Choose_hash():
	global str1
	global INPUT	
	print('Выберете хэш-функцию:'+'\n'+'"1": SHA1'+'\n'+'"2": SHA224'+'\n'+'"3": SHA256'+'\n'+'"4": SHA384'+'\n'+'"5": SHA512'+'\n'+'"6": MD5'+'\n')
	flag = input()
	
	if flag == '1':
		INPUT()
		_hash_ = _SHA1_(str1)
	elif flag == '2': 
		INPUT()
		_hash_ = _SHA224_(str1)	
	elif flag == '3': 
		INPUT()
		_hash_ = _SHA256_(str1)
	elif flag == '4': 
		INPUT()
		_hash_ = _SHA384_(str1)
	elif flag == '5': 
		INPUT()
		_hash_ = _SHA512_(str1)
	elif flag == '6': 
		INPUT()
		_hash_ = _MD5_encode(str1)
	else:
		print('ОШИБКА ВВОДА..')
		print('Ввведите заново')
		Choose_hash()
	_return_()
def Choose_encode():
	print('"1": Шифр Виженера'+'\n'+'"2": Шифр Цезаря'+'\n'+'"3": RSA'+'\n'+'"4": Base16'+'\n'+'"5": Base32'+'\n'+'"6": Base64')
	flag = input()
	if flag == '1':
		INPUT()
		key = input('Введите ключ-строку: ')
		encode_vizener(str1,key)
	elif flag =='2':
		INPUT()
		encode_caesar(str1)
	elif flag == '3':
		INPUT()
		encode_rsa(str1)		
	elif flag == '4':
		INPUT()
		_base_16(str1)
	elif flag == '5':
		INPUT()
		_base_32(str1)
	elif flag == '6':
		INPUT()
		_base_64(str1)
	else:
		print('ОШИБКА ВВОДА..'+'\n'+'Ввведите заново')
		Choose_encode()
	_return_()		
def Choose_decode():
	print('"1": Шифр Виженера'+'\n'+'"2": Шифр Цезаря'+'\n'+'"3": RSA'+'\n'+'"4": Base16'+'\n'+'"5": Base32'+'\n'+'"6": Base64')
	flag = input()
	if flag == '1' : 
		INPUT()
		print('Введите ключ-строку: ')
		key = input()
		decode_vizener(str1,key)
	elif flag =='2':
		INPUT()
		decode_caesar(str1)
	elif flag == '3':
		decode_rsa()
	elif flag == '4':
		INPUT()
		_base_d16code(str1)
	elif flag == '5':
		INPUT()
		_base_d32code(str1)
	elif flag == '6':
		INPUT()
		_base_d64code(str1)
	else:
		print('ОШИБКА ВВОДА..'+'\n'+'Ввведите заново')
		Choose_decode()
	_return_()		

if __name__ == "__main__":
	print('Вас приветствует программа, работающая с шифрами.'+'\n'+ 'К сожалению, сейчас возможна работа только с английским текстом.'+'\n'+'Выберете, что вы хотите сделать: ')
	_return_()

		
		
		
		
		
	
	