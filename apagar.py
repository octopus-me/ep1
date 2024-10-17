import pandas as pd

# Criando dois DataFrames de exemplo
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})

df2 = pd.DataFrame({
    'A': [4, 5, 6],
    'B': ['d', 'e', 'f']
})

# Concatenando os DataFrames verticalmente
resultado = pd.concat([df1, df2], ignore_index=True)

print(resultado)