import re
import pandas as pd

# Função para extrair tempo médio e intervalo de confiança de uma linha do log
def extract_time_data(line):
    match = re.search(r"([\d.,]+)\s+\+\-\s+([\d.,]+)\s+seconds time elapsed\s+\( \+\-\s+([\d.,]+)% \)", line)
    if match:
        time_mean = float(match.group(1).replace(',', '.'))
        confidence_interval = float(match.group(2).replace(',', '.'))
        confidence_percent = float(match.group(3).replace(',', '.'))
        return time_mean, confidence_interval
    return None, None

# Função para processar o arquivo de log
def process_log_file(file_path, version):
    data = []
    tamanho = 16
    with open(file_path, 'r') as file:
        for line in file:
            time_mean, confidence_interval = extract_time_data(line)
            if time_mean is not None:
                data.append([version, tamanho, time_mean, confidence_interval])
                tamanho *= 2

    # Criação de um DataFrame para organizar os dados
    df = pd.DataFrame(data, columns=["Versão", "Tamanho", "Tempo Médio (s)", "Intervalo de Confiança (s)"])
    return df

# Processamento dos logs para as três versões e concatenação dos resultados
versions = ["mandelbrot_seq", "mandelbrot_pth", "mandelbrot_omp"]
all_data = []

for version in versions:
    file_path = f'results/{version}/triple_spiral.log'
    df = process_log_file(file_path, version)
    all_data.append(df)

# Concatena todos os DataFrames em um só
final_df = pd.concat(all_data, ignore_index=True)

# Exibe o DataFrame final com todos os dados
print(final_df)

# Salva o DataFrame final em um arquivo CSV (opcional)
final_df.to_csv('elephant_summary_all_versions.csv', index=False)
