import pytest
from encriptadores import gkey, gencrypt, gdecrypt

def test_teor_probabilistico_gm():
    """
    Testamos se dois processos de encriptação da mesma mensagem gera cifras diferentes.
    Em seguida, revertemos com a decriptação e verificamos se a mensagem foi corrompida.
    """

    mensagem = "Thiago Massoni"

    n, x, p, q = gkey(128)

    emsg1 = gencrypt(mensagem, n, x)
    emsg2 = gencrypt(mensagem, n, x)

    assert emsg1 != emsg2

    dmsg1 = gdecrypt(emsg1, p, q)
    dmsg2 = gdecrypt(emsg2, p, q)

    assert dmsg1 == dmsg2
