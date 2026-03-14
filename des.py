from Crypto.Cipher import DES
from secrets import token_bytes

mensagem_secreta = "Tiago Massoni"

chave = token_bytes(8)

def encrypt(msg):
    cifra = DES.new(chave, DES.MODE_EAX)
    nonce = cifra.nonce
    texto_cifrado, tag = cifra.encrypt_and_digest(msg.encode('ascii'))
    return nonce, texto_cifrado, tag


def decrypt(nonce, texto_cifrado, tag):
    cifra = DES.new(chave, DES.MODE_EAX, nonce=nonce)
    texto = cifra.decrypt(texto_cifrado)

    try:
        cifra.verify(tag)
        return texto.decode('ascii')
    except:
        return False


nonce, texto_cifrado, tag = encrypt(mensagem_secreta)
texto = decrypt(nonce, texto_cifrado, tag)

print(f'Texto Cifrado: {texto_cifrado}')

if not texto:
    print('Mensagem corrompida!')
else:
    print(f'Texto: {texto}')
