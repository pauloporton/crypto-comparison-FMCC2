def string_para_bits(texto):
    
    bytes_texto = texto.encode('utf-8')
    bits = []

    for byte in bytes_texto:
        bits.extend([int(bit) for bit in f"{byte:08b}"])

    return bits

def bits_para_string(bits):

    chars = []
    for i in range(0, len(bits), 8):

        byte_bits = bits[i:i+8]
        byte_val = int("".join(map(str, byte_bits)), 2)
        chars.append(byte_val)
        
    return bytes(chars).decode('utf-8')

def formatar_encriptada_gm(lista_c):
    
    return ":".join([hex(c)[2:] for c in lista_c])
