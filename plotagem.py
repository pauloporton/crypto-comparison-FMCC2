import matplotlib.pyplot as plt
import pandas as pd
import json

def plotResultado(resultado, base_path):

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