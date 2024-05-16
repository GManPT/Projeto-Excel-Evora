import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Filtrar os alunos provenientes de Lisboa
alunos_lisboa = df[df['Localidade de Origem'] == 'Lisboa']

# Contar o número de alunos em cada curso
distribuicao_cursos = alunos_lisboa['Curso'].value_counts()

# Ordenar os dados para garantir uma representação adequada no gráfico de barras
distribuicao_cursos = distribuicao_cursos.sort_index()

# Desenhar o gráfico de barras
plt.figure()
distribuicao_cursos.plot(kind='bar', color='skyblue')
plt.title('Distribuição dos Alunos de Lisboa por Curso')
plt.xlabel('Curso')
plt.ylabel('Número de Alunos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico
plt.show()
