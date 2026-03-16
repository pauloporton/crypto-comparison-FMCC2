# 🔐 Crypto Comparison — FMCC2

Projeto desenvolvido como trabalho final da disciplina de **Fundamentos da Matemática para Ciência da Computação 2 (FMCC 2)** — UFCG.

O objetivo é implementar e comparar a eficiência de três algoritmos criptográficos clássicos: **DES**, **RSA** e **Goldwasser–Micali (GM)**.

---

## 👥 Integrantes

| Nome | GitHub |
|---|---|
| Caio Brito | [caio-brito-santos](https://github.com/caio-brito-santos) |
| Jefferson Stanley | [jefferson-stanley](https://github.com/jefferson-stanley) |
| Paulo Porto | [@pauloporton](https://github.com/pauloporton) |
| Pedro Barbosa | [@barbosapdr](https://github.com/barbosapdr) |
| Ricken Diniz | [@ricken-diniz](https://github.com/ricken-diniz) |

---

## 📌 Descrição

Este projeto implementa um **comparador de algoritmos criptográficos**, analisando o desempenho de cada algoritmo em diferentes tipos de entrada (senhas, palavras, frases e conteúdos extensos).

As métricas coletadas incluem:

- ⏱️ Tempo de cifragem e decifragem
- 🧠 Uso de memória RAM
- ⏰ Tempo de clock
- 📈 Complexidade Big-O estimada

As implementações dos algoritmos fazem uso de bibliotecas externas — o foco do projeto está na **camada de comparação e análise de eficiência**.

---

## 🔬 Algoritmos Comparados

### 🔷 DES — Data Encryption Standard
Cifra de bloco simétrica desenvolvida pela IBM nos anos 70 e adotada como padrão pelo NIST. Opera em blocos de 64 bits com chaves de 56 bits usando uma rede de Feistel com 16 rodadas.

### 🔶 RSA — Rivest–Shamir–Adleman
Algoritmo de criptografia assimétrica baseado na dificuldade de fatorar o produto de dois números primos grandes. Amplamente utilizado para transmissão segura de dados e assinaturas digitais.

### 🟣 GM — Goldwasser–Micali
Esquema de criptografia probabilística assimétrica baseado na dificuldade do problema da residuosidade quadrática. Notable por sua segurança provável e criptografia bit a bit.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Bibliotecas criptográficas (ex: `pycryptodome`, `cryptography`)
- `matplotlib` — geração de gráficos
- Módulos de benchmarking (`time`, `tracemalloc`)

---

## 🚀 Como Executar

### Pré-requisitos

```bash
# Clone o repositório
git clone https://github.com/pauloporton/crypto-comparison-FMCC2.git
cd crypto-comparison-FMCC2

# Instale as dependências
pip install -r requirements.txt
```

### Executar o comparador

```bash
python main.py
```

### Gerar os gráficos

```bash
python plotagem.py
```

### Executar os testes

```bash
python -m pytest tests/
```

---

## 📊 Tipos de Entrada Testados

O comparador avalia os algoritmos em quatro categorias de entrada, cada uma com seus próprios resultados armazenados:

| Categoria | Pasta de Resultados |
|---|---|
| Senhas curtas | `resultados_senhas/` |
| Palavras | `resultados_palavras/` |
| Frases | `resultados_frases/` |
| Conteúdo extenso | `resultados_conteudo_ex.../` |

Cada categoria gera os seguintes artefatos:

- `grafico_bigO.png` — complexidade estimada
- `grafico_clock.png` — tempo de clock
- `grafico_ram.png` — uso de memória RAM
- `grafico_time.png` — tempo de execução
- `resultado_*.json` — dados brutos de um teste
- `resultados_*.json` — dados agregados de múltiplos testes
- `teste_*.json` — casos de teste utilizados

---

## 📁 Estrutura do Projeto

```
crypto-comparison-FMCC2/
├── encriptadores/
│   ├── __init__.py
│   ├── des.py               # Wrapper DES
│   ├── gm.py                # Wrapper Goldwasser-Micali
│   ├── rsa.py               # Wrapper RSA
│   └── utils.py             # Utilitários compartilhados
├── resultados_conteudo_ex.../
│   ├── grafico_bigO.png
│   ├── grafico_clock.png
│   ├── grafico_ram.png
│   ├── grafico_time.png
│   └── ...
├── resultados_frases/
│   ├── grafico_bigO.png
│   ├── grafico_clock.png
│   ├── grafico_ram.png
│   ├── grafico_time.png
│   └── ...
├── resultados_palavras/
│   └── ...
├── resultados_senhas/
│   └── ...
├── tests/
│   ├── __init__.py
│   └── test_gm.py
├── .gitignore
├── __init__.py
├── comparador.py            # Lógica central de comparação
├── main.py                  # Ponto de entrada
├── plotagem.py              # Geração de gráficos
├── requirements.txt
└── README.md
```

---

## 📚 Referências

- Stallings, W. *Cryptography and Network Security*. Pearson, 2017.
- Goldwasser, S.; Micali, S. *Probabilistic Encryption*. JCSS, 1984.
- NIST FIPS PUB 46-3 — *Data Encryption Standard (DES)*.
- Rivest, R.; Shamir, A.; Adleman, L. *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*. CACM, 1978.

---

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos no âmbito da disciplina FMCC 2 — UFCG.
