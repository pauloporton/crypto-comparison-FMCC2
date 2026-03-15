from Crypto.Cipher import DES
from secrets import token_bytes


def des_key():
    bytes = 8
    return token_bytes(bytes)


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

def run(mensagem):

    key = des_key()
    nonce, encrypted, tag = encrypt(mensagem, key)
    decrypted = decrypt(nonce, encrypted, tag, key)

    return key, encrypted, decrypted
