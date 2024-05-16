import pandas as pd

# Carregar os dados do Excel
df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

# Converter a coluna 'Data de Nascimento' para datetime
df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'], errors='coerce')

# Parte A: Alunos do sexo masculino que nasceram antes de 2004 e são originários do Porto
def parte_a(df):
    # Filtrar alunos do sexo masculino, nascidos antes de 2004 e originários do Porto
    filtro_sexo = df['Sexo'] == 'M'
    filtro_data = df['Data de Nascimento'] < pd.Timestamp('2004-01-01')
    filtro_localidade = df['Localidade de Origem'] == 'Porto'

    # Aplicar os filtros
    df_filtrado = df[filtro_sexo & filtro_data & filtro_localidade]

    # Selecionar e imprimir as colunas relevantes
    resultado_a = df_filtrado[['Nome', 'Sexo', 'Data de Nascimento', 'Localidade de Origem']]
    print("Parte A:")
    print(resultado_a)
    print("\n")

# Parte B: Alunos que nasceram entre Abril e Junho, pertencem à Turma 1 e não são de Lisboa nem do Porto
def parte_b(df):
    # Função para verificar se a data de nascimento está entre abril e junho
    def nasceu_entre_abril_e_junho(data_nascimento):
        return data_nascimento.month in [4, 5, 6]

    # Filtrar alunos nascidos entre abril e junho, pertencentes à Turma 1, e que não são de Lisboa nem do Porto
    filtro_data = df['Data de Nascimento'].apply(nasceu_entre_abril_e_junho)
    filtro_turma = df['Turma'] == 'Turma1'
    filtro_localidade = ~df['Localidade de Origem'].isin(['Lisboa', 'Porto'])

    df_filtrado_b = df[filtro_data & filtro_turma & filtro_localidade]

    resultado_b = df_filtrado_b[['Nome', 'Data de Nascimento', 'Turma', 'Localidade de Origem']]
    print("Parte B:")
    print(resultado_b)

# Executar as partes A e B
parte_a(df)
parte_b(df)
