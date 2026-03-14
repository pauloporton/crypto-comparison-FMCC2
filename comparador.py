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

def metrifica_por_clock(algoritmo, mensagem, bits):
    # Métrica de clock
    
    runner = algorithms[algoritmo]

    clock_init = count()
    
    runner(mensagem, bits)

    clock_end = count_end()
    clock_elapsed = clock_end - clock_init
    
    return clock_elapsed


def metrifica_ram(algoritmo, mensagem, bits):
    #Métrica de RAM
    
    runner = algorithms[algoritmo]

    ram_init = tracemalloc.start()
    
    runner(mensagem, bits)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return peak


def metrifica_time(algoritmo, mensagem, bits):
    # Métrica de tempo
    
    runner = algorithms[algoritmo]

    time_init = time.thread_time_ns()

    runner(mensagem, bits)

    time_end = time.thread_time_ns()
    time_elapsed = time_end - time_init
    
    return time_elapsed


def metrifica_por_notacao_bigO(algoritmo, mensagem, bits):
    pass


def run_tests_with_same_bits():

    with open('teste_de_unidade.json', 'r', encoding='utf-8') as arquivo:
        bateria = json.load(arquivo)

    algoritmos = [
        "rsa",
        # "des",
        "gm"
    ]

    bits = [
        1024,
        2048
    ]


    mapeamento_de_metricas = {}
    for algoritmo in algoritmos:

        bateria_algoritmo = {}

        for bit in bits:
                
                i = 0
                bateria_algoritmo[bit] = {}
                for teste in bateria.values():

                    print(teste)

                    metricas = {}
                    metricas["time"] = metrifica_time(algoritmo, teste, bit)
                    # metricas["bigO"] = metrifica_por_notacao_bigO(algoritmo, teste, bit)
                    metricas["clock"] = metrifica_por_clock(algoritmo, teste, bit)
                    metricas["ram"] = metrifica_ram(algoritmo, teste, bit)

                    bateria_algoritmo[bit][f"teste_{i}"] = metricas
                    i+=1
        
        mapeamento_de_metricas[algoritmo] = bateria_algoritmo

    file = "resultado.json"
    
    with open(file, "w", encoding="utf-8") as f:
        json.dump(mapeamento_de_metricas, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos com sucesso em {file}!")

if __name__ == "__main__":
    run_tests_with_same_bits()



                

    