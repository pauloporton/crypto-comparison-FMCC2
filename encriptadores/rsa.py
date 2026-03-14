from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_key(bits: int = 2048):
    bits = 1024
    return RSA.generate(bits)


def rsa_encript(mensagem, chave):

    chave_publica = chave.publickey().export_key()

    chave_public_obj = RSA.import_key(chave_publica)
    cifra = PKCS1_OAEP.new(chave_public_obj)
    mensagem_encriptada = cifra.encrypt(mensagem.encode())

    return mensagem_encriptada


def rsa_decript(mensagem_encriptada, chave):

    chave_privada = chave.export_key()

    chave_privada_obj = RSA.import_key(chave_privada)
    cifra = PKCS1_OAEP.new(chave_privada_obj)
    mensagem_decriptada = cifra.decrypt(mensagem_encriptada)

    return mensagem_decriptada

def run(mensagem, bits):

    key = rsa_key(bits)
    encrypted = rsa_encript(mensagem, key)
    decrypted = rsa_decript(encrypted, key)

    return key, encrypted, decrypted