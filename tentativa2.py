import re
import pandas as pd

# Função para extrair tempo médio e intervalo de confiança de uma linha do log
def extract_time_data(line):
    match = re.search(r"([\d.,]+)\s+\+\-\s+([\d.,]+)\s+seconds time elapsed\s+\( \+\-\s+([\d.,]+)% \)", line)

    if match:
        print(match)
        time_mean = float(match.group(1).replace(',', '.'))
        print(time_mean)
        confidence_interval = float(match.group(2).replace(',', '.'))  # Intervalo direto da saída
        print(confidence_interval)
        return time_mean, confidence_interval
    return None, None

# Função para extrair tamanho da imagem e quantidade de threads da linha de comando
def extract_image_size_threads(line):
    # Expressão regular para capturar o formato específico dos valores
    pattern = r"mandelbrot_omp\s-?\d+\.\d+\s-?\d+\.\d+\s-?\d+\.\d+\s-?\d+\.\d+\s(\d+)\s(\d+)"
    match = re.search(pattern, line)
    print("OI  ", match)
    
    if match:
        # Extrai e converte os valores numéricos para inteiros
        image_size, threads = map(int, match.groups())
        print("image size", image_size)
        print("size " ,threads)
        return image_size, threads
    
    # Retorno padrão em caso de não haver correspondência
    return None, None

# Função para processar o arquivo de log
def process_log_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Verificar se a linha contém informações de imagem e threads
            if "Performance counter stats for './mandelbrot_omp" in line:
                print("ola")
                image_size, threads = extract_image_size_threads(line)
            
            # Extrair tempo médio e intervalo de confiança das linhas relevantes
            time_mean, confidence_interval = extract_time_data(line)
            if time_mean is not None and image_size is not None and threads is not None:
                data.append([image_size, threads, time_mean, confidence_interval])
    
    # Criando DataFrame para organizar os dados
    df = pd.DataFrame(data, columns=["Tamanho da Imagem", "Threads", "Tempo Médio (s)", "Intervalo de Confiança (s)"])
    return df

# Caminho do arquivo de log
file_path = 'results_threads/mandelbrot_omp/triple_spiral.log'

# Processa o arquivo e cria o DataFrame
df = process_log_file(file_path)

# Salva a tabela em CSV para análise posterior
df.to_csv('elephant_threads_summary.csv', index=False)

print("Dados processados e salvos em 'elephant_threads_summary.csv'")
print(df.head())  # Exibe as primeiras linhas para verificação
