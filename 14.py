import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Arredondar as notas de Matemática para unidades
df['Matemática'] = df['Matemática'].round()

# Calcular a tabela de frequências para Matemática
frequencias_matematica = df['Matemática'].value_counts().sort_index()

# Calcular a frequência relativa em decimal
frequencia_relativa_decimal = frequencias_matematica / len(df)

# Calcular a frequência relativa em percentagem
frequencia_relativa_percentagem = frequencia_relativa_decimal * 100

# Criar um DataFrame com as frequências
tabela_frequencias_matematica = pd.DataFrame({
    'Nota': frequencias_matematica.index,
    'Frequência Absoluta': frequencias_matematica.values,
    'Frequência Relativa (Decimal)': frequencia_relativa_decimal.values,
    'Frequência Relativa (Percentagem)': frequencia_relativa_percentagem.values
})

# Adicionar uma linha para o total
total_row = pd.DataFrame({
    'Nota': ['Total'],
    'Frequência Absoluta': [frequencias_matematica.sum()],
    'Frequência Relativa (Decimal)': [frequencia_relativa_decimal.sum()],
    'Frequência Relativa (Percentagem)': [frequencia_relativa_percentagem.sum()]
})

# Concatenar o DataFrame com a linha total
tabela_frequencias_matematica = pd.concat([tabela_frequencias_matematica, total_row], ignore_index=True)

# Converter a tabela em uma string formatada
tabela_formatada = tabulate(tabela_frequencias_matematica, headers='keys', tablefmt='grid')

# Exibir a tabela como uma imagem Matplotlib
plt.figure("Distribuições")
plt.title("Tabela de frequências das notas de Matemática")
plt.text(0.1, 0.9, tabela_formatada, {'fontsize': 10, 'fontfamily': 'monospace'})
plt.axis('off')
plt.show()
