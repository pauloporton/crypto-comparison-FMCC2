from Crypto.Util.number import getPrime, getRandomRange
from encriptadores.utils import string_para_bits, bits_para_string

def gm_keys():
    bits = 512

    while True:
        p = getPrime(bits)
        if p % 4 == 3:
            break

    while True:
        q = getPrime(bits)
        if q % 4 == 3 and q != p:
            break

    n = p * q

    while True:
        x = getRandomRange(2, n)

        if pow(x, (p-1)//2, p) == p-1 and pow(x, (q-1)//2, q) == q-1:
            break

    return n, x, p, q


def encrypt_gm(mensagem, n, x):

    mensagem_secreta = string_para_bits(mensagem)
    mensagem_encriptada = []

    for bit in mensagem_secreta:

        y = getRandomRange(1, n)

        if bit == 0:
            c = pow(y, 2, n)
        else:
            c = (x * pow(y, 2, n)) % n

        mensagem_encriptada.append(c)

    return mensagem_encriptada


def decrypt_gm(encrypted, p, q):

    mensagem_decriptada = []

    for c in encrypted:

        if pow(c, (p-1)//2, p) == 1 and pow(c, (q-1)//2, q) == 1:
            mensagem_decriptada.append(0)
        else:
            mensagem_decriptada.append(1)

    mensagem_decriptada = bits_para_string(mensagem_decriptada)

    return mensagem_decriptada

def run(mensagem):

    n, x, p, q = gm_keys()
    encrypted = encrypt_gm(mensagem, n, x)
    decrypted = decrypt_gm(encrypted, p, q)

    return n, x, p, q, encrypted, decrypted