import pandas as pd

def contem_particula_de(nome):
    return " de " in nome.strip().lower()

def nasceu_em_abril(data_nascimento):
    return data_nascimento.month == 4

df = pd.read_excel('alunos.xlsx', sheet_name='Turma A')

def imprime_de_abril():
    # Filtrar alunos com a partícula " de " no nome
    filtro_nome = df['Nome'].apply(contem_particula_de)
    df['Data de Nascimento'] = pd.to_datetime(df['Data de Nascimento'], errors='coerce')

    # Filtrar alunos que nasceram em abril
    filtro_data = df['Data de Nascimento'].apply(nasceu_em_abril)

    # Aplicar ambos os filtros
    filtro_combinados = filtro_nome & filtro_data
    df_filtrado = df[filtro_combinados]

    print("Parte A:")
    print(df_filtrado)

def primeiros_n_porto_turma2():
    # Filtrar alunos que não são do Porto e que não são da Turma 2
    filtro_localidade = df['Localidade de Origem'] != 'Porto'
    filtro_turma = df['Turma'] != 'Turma2'
    df_filtrado = df[filtro_localidade & filtro_turma]

    # Selecionar os 10 primeiros elementos
    df_top10 = df_filtrado.head(10)

    print("Parte B:")
    print(df_top10)


imprime_de_abril()
print("\n")
primeiros_n_porto_turma2()