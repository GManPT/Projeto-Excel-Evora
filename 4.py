import pandas as pd

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Filtrar os alunos originários do Porto
alunos_do_porto = df[df['Localidade de Origem'] == 'Porto']
numero_alunos_do_porto = alunos_do_porto.shape[0]

# Imprimir o resultado
print(f"Total de alunos originários do Porto: {numero_alunos_do_porto}")
