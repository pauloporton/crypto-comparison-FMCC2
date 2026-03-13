from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

mensagem_secreta = "LTC"
print("mensagem secreta: " + mensagem_secreta)

chave = RSA.generate(2048)
chave_privada = chave.export_key()
chave_publica = chave.publickey().export_key()

chave_public_obj = RSA.import_key(chave_publica)
cifra = PKCS1_OAEP.new(chave_public_obj)
mensagem_encriptada = cifra.encrypt(mensagem_secreta.encode())

print(mensagem_encriptada)

chave_privada_obj = RSA.import_key(chave_privada)
cifra = PKCS1_OAEP.new(chave_privada_obj)
mensagem_decriptada = cifra.decrypt(mensagem_encriptada)

print( mensagem_decriptada)