from plotagem import plot_metrica_media_por_tipo_teste, plot_metricas_por_algoritmos_em_colunas

if __name__ == "__main__":
    plot_metrica_media_por_tipo_teste()
    
    # Para criação de colunas
    # A variável dados informa o tipo de teste a ser executada, precisa ser inicializada (veja ex. em comparador.py)
    # plot_metricas_por_algoritmos_em_colunas(f"./resultados_{dados}/resultado_{dados}.json", f"./resultados_{dados}/")