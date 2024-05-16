import pandas as pd

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Definir a nota de aprovação
nota_de_aprovacao = 5

# Filtrar alunos aprovados em Matemática e Português, mas reprovados em História
filtro_aprovado_matematica = df['Matemática'] >= nota_de_aprovacao
filtro_aprovado_portugues = df['Português'] >= nota_de_aprovacao
filtro_reprovado_historia = df['História'] < nota_de_aprovacao

# Aplicar os filtros
df_filtrado = df[filtro_aprovado_matematica & filtro_aprovado_portugues & filtro_reprovado_historia]

# Selecionar as colunas relevantes
resultado = df_filtrado[['Número', 'Nome', 'Matemática', 'Português', 'História']]

# Imprimir o resultado
print("Alunos aprovados em Matemática e Português, mas reprovados em História:")
print(resultado)
