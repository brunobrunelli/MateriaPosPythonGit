
import csv
import pandas as pd
import json
import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercício 1:

def read_write_csv():
	df_data1 = pd.read_csv('anv.csv',sep = "~",header = 0)

	df = df_data1.aeronave_fase_operacao.value_counts().reset_index().rename(columns={'index':'aeronave_fase_operacao','aeronave_fase_operacao':'ocorrencias'})

	df['ocorrencias'] = df.ocorrencias.astype(dtype=np.float64) 

	df['percentual'] = round(df.ocorrencias.astype(dtype=np.float64) / len(df_data1) * 100,2)

	df.to_json('tmp/statistics.json', orient='records', force_ascii=False)
	
	return df_data1

def write_csv_filter(df_data1):

	df_csv = df_data1.loc[df_data1.aeronave_nivel_dano.apply(lambda x: x in ['NENHUM','LEVE'])]

	df_csv = df_csv[['aeronave_operador_categoria','aeronave_tipo_veiculo','aeronave_fabricante','aeronave_motor_tipo','aeronave_motor_quantidade','aeronave_ano_fabricacao','aeronave_assentos','total_fatalidades']]\
			.rename(columns={'aeronave_operador_categoria':'operation','aeronave_tipo_veiculo':'type','aeronave_fabricante':'manufacturer','aeronave_motor_tipo':'engine_type','aeronave_motor_quantidade':'engines','aeronave_ano_fabricacao':'year_manufacturing','aeronave_assentos':'seating','total_fatalidades':'fatalities'})

	df_csv.to_csv('tmp/levels.csv',index=False)

df_data1 = read_write_csv()
write_csv_filter(df_data1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercício 2:

pd_data2 = pd.read_csv('tmp/levels.csv', sep=',', header=0).drop_duplicates()

len(pd_data2)

pd_data2.type.value_counts().rename_axis('type').reset_index(name='quantidade acidentes')

pd_data2.year_manufacturing[pd_data2.year_manufacturing.apply(lambda x: x > 0)].min()

pd_data2[['year_manufacturing','manufacturer']].loc[pd_data2.year_manufacturing == pd_data2.year_manufacturing[pd_data2.year_manufacturing.apply(lambda x: x > 0)].min()]

pd_data2[['seating','engine_type']].loc[pd_data2.year_manufacturing == pd_data2.year_manufacturing.max()].dropna().groupby(['engine_type']).max().reset_index()

len(pd_data2.loc[(pd_data2.type.apply(lambda x: x == 'HELICÓPTERO')) & (pd_data2.year_manufacturing.apply(lambda x: x > 1997))])

len(pd_data2.loc[(pd_data2.type.apply(lambda x: x == 'AVIÃO')) & (pd_data2.manufacturer.apply(lambda x: x == 'CESSNA AIRCRAFT'))])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercício 3:

pd_data3 = pd.read_csv('cota_parlamentar_sp.csv', sep=';', header=0)

df_result = pd_data3.groupby(by=['sgpartido' , 'txnomeparlamentar'])['vlrdocumento'].sum().reset_index().rename(columns={'sgpartido':'legenda','txnomeparlamentar':'nome','vlrdocumento':'total'})

lista_partidos = df_result.legenda.drop_duplicates().tolist()

for i in lista_partidos:
    df_result[df_result.legenda == i].to_json('tmp\\'+i+'.json',orient='records', force_ascii=False)
