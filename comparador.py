from hwcounter import count, count_end
import tracemalloc
from encriptadores import rkey, dkey, gkey, rencrypt, dencrypt, gencrypt, rdecrypt, ddecrypt, gdecrypt, rrun, drun, grun
import time
import json

algorithms = {
    "rsa" : rrun,
    "des" : drun,
    "gm" : grun
}

def metrifica_por_clock(algoritmo, mensagem):
    # Métrica de clock
    
    runner = algorithms[algoritmo]

    clock_init = count()
    
    runner(mensagem)

    clock_end = count_end()
    clock_elapsed = clock_end - clock_init
    
    return clock_elapsed


def metrifica_ram(algoritmo, mensagem):
    #Métrica de RAM
    
    runner = algorithms[algoritmo]

    ram_init = tracemalloc.start()
    
    runner(mensagem)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak


def metrifica_time(algoritmo, mensagem):
    # Métrica de tempo
    
    runner = algorithms[algoritmo]

    time_init = time.thread_time_ns()

    runner(mensagem)

    time_end = time.thread_time_ns()
    time_elapsed = time_end - time_init
    
    return time_elapsed


def metrifica_por_notacao_bigO(algoritmo, mensagem):
    
    complexidade = 0
    if(algoritmo == "rsa"):

        # A parte mais densa do algoritmo é gerar números aleatórios e verificar se são, primos, por
        # convenção, vamos assumir que esta parte irá ser O(n³)
        complexidade_gerar_chave =  2048**3

        # Pela equação c = m^k (mod N) temos que levar em consideração a exponenciação do expoente de 
        # encriptação O(k) ou O(log(k)) com exponenciação binária, mais o número de multiplicações bit
        #  a bit das chaves p e q, que, por convenção, vamos assumir que possuem o mesmo tamanho de N 
        # (2048 neste estudo), logo, para encriptar, temos log(k)*n², que será multiplicado por m (tamanho
        # em bits da mensagem) / n, que significa o tamanho de cada chunk, resultando em m * n * log(k),
        # sendo k um valor muito pequeno.
        complexidade_encriptar = (len(mensagem.encode("utf-8") * 8)) * 2048
    
        # Complexidade para decriptar é similar a complexidade de encriptar, visto que vem a partir da
        # fórmula m = c^d (mod N), porém, d é o expoente de decriptação que pode extremamente grande,
        # tendo o cálculo de sua potência similar a O(n), transpondo de m * n * log(k) para m * n²
        complexidade_decriptar = (len(mensagem.encode("utf-8") * 8)) * 2048 * 2048

        return complexidade_gerar_chave + complexidade_encriptar + complexidade_decriptar

    if(algoritmo == "gm"):
        
        # A parte mais densa do algoritmo é gerar números aleatórios e verificar se são, primos, por
        # convenção, vamos assumir que esta parte irá ser O(n³)
        complexidade_gerar_chave =  512**3

        # O GM trabalha em operação bit a bit, logo, temos que considerar o tamanho O(m) da mensagem
        # que será multiplicado pela complexidade total. A partir da fórmula ci = y²*x^mi, temos, a
        # exponenciação e a geração de números aleatórios escalam o algoritmo em aproximadamente O(n³). 
        # Totalizando, temos O(m*n³)
        complexidade_encriptar = (512**3) * (len(mensagem.encode("utf-8") * 8))

        # A partir da fórmula L = ci^[(p-1)/2] (mod p), temos operações similares de exponenciação modular
        # pelo número de p, que pode ter quase tantos bits que n, sendo uma operação tão custosa quando a 
        # encriptação
        complexidade_decriptar = (512**3) * (len(mensagem.encode("utf-8") * 8))

        return complexidade_gerar_chave + complexidade_encriptar + complexidade_decriptar
    
    if(algoritmo == "des"):

        # Com base nos estudos feitos, o DES praticamente não tem custos com sua geração de chaves, tendo
        # apenas gastos de encriptação e decriptação com base no tamanho da chave utilizada. A encriptação
        # e decriptação é feita em cima de blocos das mensagens com operações básicas como XOR, a partir da
        # chave gerada, resultando em O(m) cada.
        complexidade = 2 * len(mensagem.encode("utf-8")) * 8

        return complexidade


def run_tests_with_same_bits(dados_path, resultados_path):

    with open(dados_path, 'r', encoding='utf-8') as arquivo:
        bateria = json.load(arquivo)

    algoritmos = [
        "rsa",
        "des",
        "gm"
    ]


    mapeamento_de_metricas = {}
    for algoritmo in algoritmos:

        bateria_algoritmo = {}
                
        i = 0
        bateria_algoritmo = {}
        print(algoritmo)
        for teste in bateria.values():

            print(f"teste_{i}", end="", flush=True)

            metricas = {}
            metricas["time"] = metrifica_time(algoritmo, teste)
            metricas["bigO"] = metrifica_por_notacao_bigO(algoritmo, teste)
            metricas["clock"] = metrifica_por_clock(algoritmo, teste)
            metricas["ram"] = metrifica_ram(algoritmo, teste)

            print("✅")

            bateria_algoritmo[f"teste_{i}"] = metricas
            i+=1
        
        mapeamento_de_metricas[algoritmo] = bateria_algoritmo
    
    with open(resultados_path, "w", encoding="utf-8") as f:
        json.dump(mapeamento_de_metricas, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos com sucesso em {resultados_path}!")

if __name__ == "__main__":
    dados = "conteudo_extenso"
    run_tests_with_same_bits(f"./resultados_{dados}/teste_{dados}.json", f"./resultados_{dados}/resultado_{dados}.json")



                

    