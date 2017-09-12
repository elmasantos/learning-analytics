#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

from estatisticas import *

def medias():
	media_ate_1_salario = media_de_dado(ate_1_salario)
	print("\nMédia de renda familiar de até 1 salário mínimo: ",
		media_ate_1_salario)

	media_mais_1_ate_5 = media_de_dado(mais_de_1_ate_5)
	print("Média de renda familiar de mais de 1 até 5 salários mínimos: ",
		media_mais_1_ate_5)

	media_mais_5_ate_10 = media_de_dado(mais_de_5_ate_10)
	print("Média de renda familiar de mais de 5 até 10 salários mínimos: ",
		media_mais_5_ate_10)

	media_mais_de_10_ate_20 = media_de_dado(mais_de_10_ate_20)
	print("Média de renda familiar de mais de 10 até 20 salários mínimos: ",
		media_mais_de_10_ate_20)

	media_mais_de_20 = media_de_dado(mais_de_20)
	print("Média de renda familiar de mais de 20 salários mínimos: ",
		media_mais_de_20)

	media_nao_se_aplica = media_de_dado(nao_se_aplica)
	print("Média de renda familiar 'não se aplica': ",
		media_nao_se_aplica)

	media_nao_respondeu = media_de_dado(nao_respondeu)
	print("Média de renda familiar 'não respondeu': ",
		media_nao_respondeu)		


def medianas():
	mediana_ate_1_salario = mediana(ate_1_salario)
	print("\nMediana de renda familiar de até 1 salário mínimo: ",
		mediana_ate_1_salario)

	mediana_mais_1_ate_5 = mediana(mais_de_1_ate_5)
	print("Mediana de renda familiar de mais de 1 até 5 salários mínimos: ",
		mediana_mais_1_ate_5)

	mediana_mais_5_ate_10 = mediana(mais_de_5_ate_10)
	print("Mediana de renda familiar de mais de 5 até 10 salários mínimos: ",
		mediana_mais_5_ate_10)

	mediana_mais_de_10_ate_20 = mediana(mais_de_10_ate_20)
	print("Mediana de renda familiar de mais de 10 até 20 salários mínimos: ",
		mediana_mais_de_10_ate_20)

	mediana_mais_de_20 = mediana(mais_de_20)
	print("Mediana de renda familiar de mais de 20 salários mínimos: ",
		mediana_mais_de_20)

	mediana_nao_se_aplica = mediana(nao_se_aplica)
	print("Mediana de renda familiar 'não se aplica': ",
		mediana_nao_se_aplica)

	mediana_nao_respondeu = mediana(nao_respondeu)
	print("Mediana de renda familiar 'não respondeu': ",
		mediana_nao_respondeu)

def amplitudes():
	print("\nAté 1 salário mínimo:")
	amplitude(ate_1_salario)

	print("Mais de 1 até 5 salários mínimos:")
	amplitude(mais_de_1_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	amplitude(mais_de_5_ate_10)

	print("Mais de 10 até 20 salários mínimos:")
	amplitude(mais_de_10_ate_20)

	print("Mais de 20 salários mínimos:")
	amplitude(mais_de_20)

	print("Não se aplica:")
	amplitude(nao_se_aplica)

	print("Não respondeu:")
	amplitude(nao_respondeu)

def modas():
	print("\nAté 1 salário mínimo:")
	moda_dado(ate_1_salario)

	print("Mais de 1 até 5 salários mínimos:")
	moda_dado(mais_de_1_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	moda_dado(mais_de_5_ate_10)

	print("Mais de 10 até 20 salários mínimos:")
	moda_dado(mais_de_10_ate_20)

	print("Mais de 20 salários mínimos:")
	moda_dado(mais_de_20)

	print("Não se aplica:")
	moda_dado(nao_se_aplica)

	print("Não respondeu:")
	moda_dado(nao_respondeu)	

def desvios_padrao():
	print("\nAté 1 salário mínimo:")
	desvio_padrao(ate_1_salario)

	print("Mais de 1 até 5 salários mínimos:")
	desvio_padrao(mais_de_1_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	desvio_padrao(mais_de_5_ate_10)

	print("Mais de 10 até 20 salários mínimos:")
	desvio_padrao(mais_de_10_ate_20)

	print("Mais de 20 salários mínimos:")
	desvio_padrao(mais_de_20)

	print("Não se aplica:")
	desvio_padrao(nao_se_aplica)

	print("Não respondeu:")
	desvio_padrao(nao_respondeu)

colnames =["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"]
renda_mensal_familiar = pd.read_csv('fisica/FISICA-GENERO_X_RENDA_MENSAL_FAMILIA.csv',  names = colnames)

variaveis = renda_mensal_familiar.col1[1:].tolist()
ate_1_salario = renda_mensal_familiar.col2[1:].tolist()
mais_de_1_ate_5 = renda_mensal_familiar.col3[1:].tolist()
mais_de_5_ate_10 = renda_mensal_familiar.col4[1:].tolist()
mais_de_10_ate_20 = renda_mensal_familiar.col5[1:].tolist()
mais_de_20 = renda_mensal_familiar.col6[1:].tolist()
nao_se_aplica = renda_mensal_familiar.col7[1:].tolist()
nao_respondeu = renda_mensal_familiar.col8[1:].tolist()
total = renda_mensal_familiar.col9[1:].tolist()

medias()
medianas()
amplitudes()
modas()
desvios_padrao()

