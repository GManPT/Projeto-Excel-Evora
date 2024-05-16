import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Selecionar as colunas das disciplinas
disciplinas = ['Português', 'Matemática', 'História']

# Calcular a média para cada disciplina
medias = df[disciplinas].mean()

# Criar o gráfico de barras
plt.figure()
medias.plot(kind='bar', color=['#66b3ff','#ff9999','#99ff99'])
plt.title('Média Final por Disciplina')
plt.xlabel('Disciplina')
plt.ylabel('Média Final por Disciplina')
plt.xticks(rotation=0)
plt.ylim(0, 5.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.show()
