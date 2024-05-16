import pandas as pd

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Converter a coluna 'Data de Nascimento' para datetime
df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'])

# Filtrar os alunos com "Silva" no nome e nascidos antes de 2004
filtro_nome = df['Nome'].str.contains('Silva', case=False)
filtro_data = df['Data de Nascimento'] < pd.Timestamp('2004-01-01')
alunos_silva = df[filtro_nome & filtro_data]

# Selecionar e imprimir as colunas relevantes
resultado = alunos_silva[['Nome', 'Data de Nascimento', 'Localidade de Origem']]
print(resultado)
