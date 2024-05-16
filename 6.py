import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Contar a quantidade de cada situação
situacao_counts = df['Situação'].value_counts()

# Criar o gráfico de pizza
plt.figure()
situacao_counts.plot(kind='pie', autopct='%1.1f%%', colors=["#ff9999","#99ff99"])
plt.title('Distribuição da Situações')
plt.ylabel('')

# Exibir o gráfico
plt.show()