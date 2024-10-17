import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do CSV
# Substitua o caminho abaixo pelo local do seu arquivo CSV
csv_file = 'elephant_threads_summary.csv'
data = pd.read_csv(csv_file)

# Ignorar a coluna 'Intervalo de Confiança (s)'
data = data.drop(columns=['Intervalo de Confiança (s)'])

# Configurações do gráfico
plt.figure(figsize=(10, 6))
threads_list = sorted(data['Threads'].unique())
colors = ['b', 'g', 'r', 'c', 'm']  # Cores para diferentes números de threads

# Gerar o gráfico para cada valor de 'Threads'
for i, threads in enumerate(threads_list):
    subset = data[data['Threads'] == threads]
    plt.plot(subset['Tamanho da Imagem'], subset['Tempo Médio (s)'], label=f'{threads} Threads', color=colors[i], marker='o')

# Configurações de escala logarítmica para ambos os eixos
plt.xscale('log')
plt.yscale('log')

# Título e rótulos dos eixos
plt.title('Comparação do Tempo Médio de Execução em Função do Tamanho da Imagem e Número de Threads (Região Triple Spiral)')
plt.xlabel('Tamanho da Imagem')
plt.ylabel('Tempo Médio de Execução (s)')

# Legenda
plt.legend(title='Número de Threads')

# Adicionando grade ao gráfico para melhor visualização
plt.grid(True, which="both", ls="--")

# Salvar o gráfico em um arquivo .png
plt.savefig('comparacao_tempo_medio_execucao.png', dpi=300)

# Exibir o gráfico
plt.show()
