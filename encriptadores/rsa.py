from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_key():
    bits = 2048
    return RSA.generate(bits)


def rsa_encript(mensagem, chave, margem_de_seguranca=10):

    mensagem = mensagem.encode("utf-8")

    chave_publica = chave.publickey().export_key()

    chave_public_obj = RSA.import_key(chave_publica)
    cifra = PKCS1_OAEP.new(chave_public_obj)

    chunk_size = chave_public_obj.size_in_bytes()
    
    if len(mensagem) > chunk_size:
        # Chunks com margem de erro para frases não tratadas, uma vez que um caractere especial pode ocupar mais de um byte
        padding_overhead = 42
        chunk_size = chave_public_obj.size_in_bytes() - padding_overhead - margem_de_seguranca

    if chunk_size <= 0:
            raise ValueError("A chave é pequena demais para o padding e a margem escolhida.")
    
    mensagem_encriptada_em_chunks = []
    for i in range(0, len(mensagem), chunk_size):
        chunk = mensagem[i:i + chunk_size]
        mensagem_encriptada_em_chunks.append(cifra.encrypt(chunk))
    
    mensagem_encriptada = b"".join(mensagem_encriptada_em_chunks)
    return mensagem_encriptada


def rsa_decript(mensagem_encriptada, chave):

    chave_privada = chave.export_key()
    chave_privada_obj = RSA.import_key(chave_privada)
    cifra = PKCS1_OAEP.new(chave_privada_obj)

    key_size = chave_privada_obj.size_in_bytes()
    mensagem_decriptada_em_chunks = []

    for i in range(0, len(mensagem_encriptada), key_size):
        chunk = mensagem_encriptada[i:i + key_size]
        mensagem_decriptada_em_chunks.append(cifra.decrypt(chunk))
    
    mensagem_decriptada = b"".join(mensagem_decriptada_em_chunks)

    return mensagem_decriptada

def run(mensagem):

    key = rsa_key()
    encrypted = rsa_encript(mensagem, key)
    decrypted = rsa_decript(encrypted, key)

    return key, encrypted, decrypted