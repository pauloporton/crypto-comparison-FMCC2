from Crypto.Cipher import DES
from secrets import token_bytes


def des_key(bits: int = 8):
    bits = 8
    return token_bytes(bits)


def encrypt(mensagem, chave):

    cifra = DES.new(chave, DES.MODE_EAX)
    nonce = cifra.nonce
    texto_cifrado, tag = cifra.encrypt_and_digest(mensagem.encode('ascii'))
    return nonce, texto_cifrado, tag


def decrypt(nonce, texto_cifrado, tag, chave):

    cifra = DES.new(chave, DES.MODE_EAX, nonce=nonce)
    texto = cifra.decrypt(texto_cifrado)

    try:
        cifra.verify(tag)
        return texto.decode('ascii')
    except:
        return False

def run(mensagem, bits):

    key = des_key(bits)
    nonce, encrypted, tag = encrypt(mensagem, key)
    decrypted = decrypt(nonce, encrypted, tag, key)

    return key, encrypted, decrypted
