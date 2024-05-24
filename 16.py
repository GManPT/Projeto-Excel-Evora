import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Arredondar as notas de Matemática para unidades
df['Matemática'] = df['Matemática'].round()

# Calcular a tabela de frequências para Matemática
frequencias_matematica = df['Matemática'].value_counts().sort_index()

# Plotar o gráfico circular
plt.figure("Grafico Circular")
plt.pie(frequencias_matematica, labels=frequencias_matematica.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Gráfico Circular das Notas de Matemática')
plt.axis('equal')
plt.tight_layout()
plt.show()

