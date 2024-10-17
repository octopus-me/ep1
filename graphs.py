import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados do arquivo CSV
data = pd.read_csv('elephant_summary_all_versions.csv')

# Definindo o gráfico
plt.figure(figsize=(10, 6))

# Listagem das versões para iteração
versions = data['Versão'].unique()

# Gráficos de linha para cada versão com barras de erro (intervalo de confiança)
for version in versions:
    version_data = data[data['Versão'] == version]
    plt.errorbar(
        version_data['Tamanho'], 
        version_data['Tempo Médio (s)'], 
        yerr=version_data['Intervalo de Confiança (s)'], 
        label=version, 
        capsize=5,
        marker='o'
    )

# Configuração dos rótulos e título do gráfico
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo Médio de Execução (s)')
plt.title('Tempo Médio de Execução para Diferentes Versões de Mandelbrot (Triple Spiral)')
plt.legend(title="Versão")
plt.grid(True)



# Exibição do gráfico
plt.tight_layout()
plt.savefig('grafico_mandelbrot_1thread_full.png', dpi=300)  # Você pode mudar o nome e o formato se desejar


