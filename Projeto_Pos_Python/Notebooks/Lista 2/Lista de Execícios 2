
# # Lista de Execícios 2
# #### Exercício 1:

import csv
import pandas as pd
import json

df_data1 = pd.read_csv('anv.csv',sep = "~",header = 0)

    # df_fase = df_data.aeronave_fase_operacao.value_counts().rename_axis('aeronave_fase_operacao').reset_index(name='quantidade')
    # df_fase['percentual'] = (df_fase.quantidade / len(df_data)) * 100

    dic = df_data1.groupby(by='aeronave_fase_operacao').size().rename_axis('aeronave_fase_operacao').sort_values(ascending=False).to_dict()

    lista = []

    for key,value in dic.items():
        lista.append({'fase_operacao':key,'ocorrencias':value, 'percentual': round((value/len(df_data1)) * 100,2)})

    with open('tmp/statistics.json','w') as f:
    json.dump(lista,f)

    df_csv = df_data1.loc[df_data.aeronave_nivel_dano.apply(lambda x: x in ['NENHUM','LEVE'])]

    df_csv = df_csv[['aeronave_operador_categoria',\
                     'aeronave_tipo_veiculo',\
                     'aeronave_fabricante',\
                     'aeronave_motor_tipo',\
                     'aeronave_motor_quantidade',\
                     'aeronave_ano_fabricacao',\
                     'aeronave_assentos',\
                     'total_fatalidades']]\
    .rename(columns={'aeronave_operador_categoria':'operation',\
                     'aeronave_tipo_veiculo':'type',\
                     'aeronave_fabricante':'manufacturer',\
                     'aeronave_motor_tipo':'engine_type',\
                     'aeronave_motor_quantidade':'engines',\
                     'aeronave_ano_fabricacao':'year_manufacturing',\
                     'aeronave_assentos':'seating',\
                     'total_fatalidades':'fatalities'})

    df_csv.to_csv('tmp/levels.csv',index=False)

# --------------------------------------------------------------------------------------------------------------------------------------------------
   
# #### Execício 2:

# ### Crie um programa que efetue a leitura do arquivo produzido no exercício 1 (levels.csv) e mostre na tela as seguintes informações estatísticas:
# * Quantidade total de acidentes
# * Quantidade total de acidentes agrupados por tipo de aeronave (type)
# * Ano e fabricante da aeronave mais antiga (year_manufacturing, manufacturer)
# * Quantidade de assentos e tipo de motor da aeronave mais nova (seating, engine_type)
# * A quantidade de acidentes que ocorreram com aeronaves do tipo (type) HELICÓPTERO, cuja fabricação se deu após o ano 1997
# * A quantidade de acidentes que ocorreram com aeronaves do tipo (type) AVIÃO fabricadas (manufacturer) pela CESSNA AIRCRAFT
# 
# OBS: 
# 1. Efetuar todas as leituras e gravações de arquivos na pasta /tmp

pd_data2 = pd.read_csv('tmp/levels.csv', sep=',', header=0).drop_duplicates()

# Quantidade total de acidentes
total_acidentes = len(pd_data2)

# Quantidade total de acidentes agrupados por tipo de aeronave (type)
qtd_acidentes_type = pd_data2.type.value_counts().rename_axis('type').reset_index(name='quantidade acidentes')

#Ano e fabricante da aeronave mais antiga (year_manufacturing, manufacturer)
min_val = pd_data2.year_manufacturing[pd_data2.year_manufacturing.apply(lambda x: x > 0)].min()

old_fabricante = pd_data2[['year_manufacturing','manufacturer']]\
.loc[pd_data2.year_manufacturing == pd_data2.year_manufacturing[pd_data2.year_manufacturing.apply(lambda x: x > 0)].min()]

# Quantidade de assentos e tipo de motor da aeronave mais nova (seating, engine_type)
qtd_aero_motor = pd_data2[['seating','engine_type']].loc[pd_data2.year_manufacturing == pd_data2.year_manufacturing.max()]\
.dropna().groupby(['engine_type']).max().reset_index()
