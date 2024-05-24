import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Arredondar as notas de Matemática para unidades
df['Matemática'] = df['Matemática'].round()

# Calcular a tabela de frequências para Matemática
frequencias_matematica = df['Matemática'].value_counts().sort_index()

# Plotar o gráfico de barras
plt.figure("Grafico de Barras")
frequencias_matematica.plot(kind='bar', color='skyblue')
plt.title('Gráfico de Barras das Notas de Matemática')
plt.xlabel('Nota')
plt.ylabel('Frequência Absoluta')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
