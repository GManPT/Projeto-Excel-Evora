import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Calcular o número de alunos por localidade de origem
alunos_por_localidade = df['Localidade de Origem'].value_counts()

# Selecionar as 5 localidades com mais alunos
top5_localidades = alunos_por_localidade.head(5)

# Gerar um gráfico de pizza com as 5 localidades destacadas
plt.figure()
top5_localidades.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
plt.title('Distribuição dos Alunos por Localidade (Top 5)')
plt.ylabel('')  # Remover o rótulo do eixo y

# Exibir o gráfico
plt.show()
