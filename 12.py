import pandas as pd

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Codificar a variável categórica 'Curso' usando one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Curso'])

# Selecionar as colunas de interesse: valor da propina, média final e todas as colunas de curso
colunas_interesse = ['Valor da Propina', 'Média Final'] + [coluna for coluna in df_encoded.columns if 'Curso_' in coluna]
dados_interesse = df_encoded[colunas_interesse]

# Calcular o coeficiente de correlação de Pearson
correlacao = dados_interesse.corr(method='pearson')

# Exibir a matriz de correlação
print("Matriz de Correlação:")
print(correlacao)
