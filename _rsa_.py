#-*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
def keygen():	
	code = input('Придумайте и введите секретное слово: ')
	key = RSA.generate(2048)
	encrypted_key = key.exportKey(passphrase=code, pkcs=8,protection="scryptAndAES128-CBC")
	with open('my_private_rsa_key.bin', 'wb') as f:
		f.write(encrypted_key)
	with open('my_rsa_public.pem', 'wb') as f:
			f.write(key.publickey().exportKey())
def encode_rsa_(data): 
	print('Начинаем шифрование..'+'\n'+'Зашифрованное сообщение будет лежать в файле "encrypted_data.bin"')
	with open('encrypted_data.bin', 'wb') as out_file:
		recipient_key = RSA.importKey(open('my_rsa_public.pem').read())
		session_key = get_random_bytes(16)
		cipher_rsa = PKCS1_OAEP.new(recipient_key)
		out_file.write(cipher_rsa.encrypt(session_key))
		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		data= bytes(data,encoding=('utf-8'))
		ciphertext, tag = cipher_aes.encrypt_and_digest(data)
		out_file.write(cipher_aes.nonce)
		out_file.write(tag)
		out_file.write(ciphertext)
		print('Готово!')
def decode_rsa():
	print('Начинаем расшифровку..')
	print('Зашифрованное сообщение должно лежать в файле "encrypted_data.bin", a ключ в "my_private_rsa_key.bin"')
	code = input('Введите секретное слово: ')
	try:
		with open('encrypted_data.bin', 'rb') as fobj:
			private_key = RSA.import_key(open('my_private_rsa_key.bin').read(),passphrase=code)
			enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
														for x in (private_key.size_in_bytes(), 
														16, 16, -1) ]
			cipher_rsa = PKCS1_OAEP.new(private_key)
			session_key = cipher_rsa.decrypt(enc_session_key)
			cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
			data = cipher_aes.decrypt_and_verify(ciphertext, tag)
		print('Результат: ')
		print(data)
	except:
		print('Ошибка! Проверьте наличие ключа и текста в указанных файлах и попробуйте еще раз:')
		decode_rsa()
def encode_rsa(data):
	flag = input('"1"- Для использования готового ключа'+'\n'+'В любом другом случае будет сгенерирован новых ключ'+'\n')
	if flag == 1: encode_rsa_(data)
	else:keygen();	encode_rsa_(data)
	