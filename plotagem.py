import matplotlib.pyplot as plt
import pandas as pd
import json
import copy

def plot_metrica_media_por_tipo_teste():
    modelo_base = {
         "rsa" : {
              "senhas" : 0,
              "palavras" : 0,
              "frases" : 0,
            #   "conteudo_extenso" : 0
         },
         "des" : {
              "senhas" : 0,
              "palavras" : 0,
              "frases" : 0,
            #   "conteudo_extenso" : 0
         },
         "gm" : {
              "senhas" : 0,
              "palavras" : 0,
              "frases" : 0,
            #   "conteudo_extenso" : 0
         }
    }

    metricas = {
         "time": copy.deepcopy(modelo_base),
         "bigO": copy.deepcopy(modelo_base),
         "ram": copy.deepcopy(modelo_base),
         "clock": copy.deepcopy(modelo_base)
    }

    # tipos_teste = ["senhas", "palavras", "conteudo_extenso", "frases"]
    tipos_teste = ["senhas", "palavras", "frases"]
    for tipo_teste in tipos_teste:
        with open(f"resultados_{tipo_teste}/resultado_{tipo_teste}.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            size = 0
            for alg in data.keys():
                size = len(data[alg].values())
                for teste in data[alg].values():
                    for metrica in teste.keys():
                        metricas[metrica][alg][tipo_teste] += teste[metrica]

            for metrica in metricas.keys():
                for alg in metricas[metrica].keys():
                    metricas[metrica][alg][tipo_teste] = metricas[metrica][alg][tipo_teste] / size
    
    
    algoritmos = ["rsa", "des", "gm"]
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Análise de Performance de Algoritmos', fontsize=16)

    plot_info = [
        ("time", "Tempo de Execução (ms)", axes[0, 0]),
        ("bigO", "Complexidade (Operações)", axes[0, 1]),
        ("ram", "Consumo de RAM (MB)", axes[1, 0]),
        ("clock", "Ciclos de Clock", axes[1, 1])
    ]

    for m_key, titulo, ax in plot_info:
        for alg in algoritmos:
            valores = [metricas[m_key][alg][tipo_teste] for tipo_teste in tipos_teste]
            ax.plot(tipos_teste, valores, marker='o', label=alg.upper())
        
        ax.set_title(titulo)
        ax.set_ylabel('Valor da Métrica')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f'grafico_linhas.png')
    plt.close()

                
    

def plot_metricas_por_algoritmos_em_colunas(resultado, base_path):

    with open(resultado, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = []
    for algo, testes in data.items():
            for teste_id, metricas in testes.items():
                rows.append({
                    'label': f"{algo}_{teste_id}",
                    'algoritmo': algo,
                    'time': metricas.get('time', 0),
                    'clock': metricas.get('clock', 0),
                    'ram': metricas.get('ram', 0),
                    'bigO': metricas.get('bigO', 0)
                })

    df = pd.DataFrame(rows)

    # Mapeamento de cores solicitado
    cores_map = {'rsa': 'red', 'des': 'green', 'gm': 'blue'}
    df['color'] = df['algoritmo'].map(cores_map)

    # Configurações das métricas para os 4 gráficos
    metricas_alvo = [
        ('time', 'Tempo de Execução (s)'),
        ('clock', 'Ciclos de CPU (Clock)'),
        ('ram', 'Consumo de RAM (KB)'),
        ('bigO', 'Estimativa em Big O (ciclos)')
    ]

    # 3. Gerar os 4 gráficos
    for i, (col, titulo) in enumerate(metricas_alvo, 1):
        plt.figure(figsize=(12, 6))
        
        bars = plt.bar(df['label'], df[col], color=df['color'])
        
        plt.title(titulo, fontsize=14)
        plt.xlabel('Algoritmo / Teste', fontsize=12)
        plt.ylabel(titulo, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], color='red', lw=4, label='RSA'),
                        Line2D([0], [0], color='green', lw=4, label='DES'),
                        Line2D([0], [0], color='blue', lw=4, label='GM')]
        plt.legend(handles=legend_elements)
        
        plt.tight_layout()
        plt.savefig(f'{base_path}grafico_{col}.png')
        plt.close()

    print("Gráficos gerados com sucesso: grafico_time.png, grafico_clock.png, grafico_ram.png e _undefined")