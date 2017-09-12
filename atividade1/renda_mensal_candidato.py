#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

from estatisticas import *

def medias():
	media_nao_tem_renda = media_de_dado(nao_tem_renda)
	print("\nMédia de renda familiar de não tem renda: ",
		media_nao_tem_renda)

	media_mais_1_ate_5 = media_de_dado(ate_1_salario)
	print("Média de renda familiar de até 1 salário mínimo: ",
		media_mais_1_ate_5)

	media_mais_5_ate_10 = media_de_dado(mais_de_1_ate_2)
	print("Média de renda familiar de mais de 1 até 2 salários mínimos: ",
		media_mais_5_ate_10)

	media_mais_de_2_ate_5 = media_de_dado(mais_de_2_ate_5)
	print("Média de renda familiar de mais de 2 até 5 salários mínimos: ",
		media_mais_de_2_ate_5)

	media_mais_de_5_ate_10 = media_de_dado(mais_de_5_ate_10)
	print("Média de renda familiar de mais de 5 até 10 salários mínimos: ",
		media_mais_de_5_ate_10)

	media_mais_de_10 = media_de_dado(mais_de_10)
	print("Média de renda familiar mais de 10 salários mínimos: ",
		media_mais_de_10)

	media_nao_respondeu = media_de_dado(nao_respondeu)
	print("Média de renda familiar 'não respondeu': ",
		media_nao_respondeu)		


def medianas():
	mediana_nao_tem_renda = mediana(nao_tem_renda)
	print("\nMediana de renda familiar de não tem renda: ",
		mediana_nao_tem_renda)

	mediana_mais_1_ate_5 = mediana(ate_1_salario)
	print("Mediana de renda familiar de até 1 salário mínimo: ",
		mediana_mais_1_ate_5)

	mediana_mais_5_ate_10 = mediana(mais_de_1_ate_2)
	print("Mediana de renda familiar de mais de 1 até 2 salários mínimos: ",
		mediana_mais_5_ate_10)

	mediana_mais_de_2_ate_5 = mediana(mais_de_2_ate_5)
	print("Mediana de renda familiar de mais de 2 até 5 salários mínimos: ",
		mediana_mais_de_2_ate_5)

	mediana_mais_de_5_ate_10 = mediana(mais_de_5_ate_10)
	print("Mediana de renda familiar de mais de 5 até 10 salários mínimos: ",
		mediana_mais_de_5_ate_10)

	mediana_mais_de_10 = mediana(mais_de_10)
	print("Mediana de renda familiar de mais de 10 salários mínimos: ",
		mediana_mais_de_10)

	mediana_nao_respondeu = mediana(nao_respondeu)
	print("Mediana de renda familiar 'não respondeu': ",
		mediana_nao_respondeu)

def amplitudes():
	print("\nNão tem renda:")
	amplitude(nao_tem_renda)

	print("Até 1 salário mínimo:")
	amplitude(ate_1_salario)

	print("Mais de 1 até 2 salários mínimos:")
	amplitude(mais_de_1_ate_2)

	print("Mais de 2 até 5 salários mínimos:")
	amplitude(mais_de_2_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	amplitude(mais_de_5_ate_10)

	print("Mais de 10 salários mínimos:")
	amplitude(mais_de_10)

	print("Não respondeu:")
	amplitude(nao_respondeu)

def modas():
	print("\nNão tem renda:")
	moda_dado(nao_tem_renda)

	print("Até 1 salário mínimo:")
	moda_dado(ate_1_salario)

	print("Mais de 1 até 2 salários mínimos:")
	moda_dado(mais_de_1_ate_2)

	print("Mais de 2 até 5 salários mínimos:")
	moda_dado(mais_de_2_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	moda_dado(mais_de_5_ate_10)

	print("Mais de 10 salários mínimos:")
	moda_dado(mais_de_10)

	print("Não respondeu:")
	moda_dado(nao_respondeu)	

def desvios_padrao():
	print("\nNão tem renda:")
	desvio_padrao(nao_tem_renda)

	print("Até 1 salário mínimo:")
	desvio_padrao(ate_1_salario)

	print("Mais de 1 até 2 salários mínimos:")
	desvio_padrao(mais_de_1_ate_2)

	print("Mais de 2 até 5 salários mínimos:")
	desvio_padrao(mais_de_2_ate_5)

	print("Mais de 5 até 10 salários mínimos:")
	desvio_padrao(mais_de_5_ate_10)

	print("Mais de 10 salários mínimos:")
	desvio_padrao(mais_de_10)

	print("Não respondeu:")
	desvio_padrao(nao_respondeu)

colnames =["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"]
renda_mensal_candidato = pd.read_csv('fisica/FISICA-GENERO_X_RENDA_MENSAL_CANDIDATO.csv',  names = colnames)

variaveis = renda_mensal_candidato.col1[1:].tolist()
nao_tem_renda = renda_mensal_candidato.col2[1:].tolist()
ate_1_salario = renda_mensal_candidato.col3[1:].tolist()
mais_de_1_ate_2 = renda_mensal_candidato.col4[1:].tolist()
mais_de_2_ate_5 = renda_mensal_candidato.col5[1:].tolist()
mais_de_5_ate_10 = renda_mensal_candidato.col6[1:].tolist()
mais_de_10 = renda_mensal_candidato.col7[1:].tolist()
nao_respondeu = renda_mensal_candidato.col8[1:].tolist()
total = renda_mensal_candidato.col9[1:].tolist()

medias()
medianas()
amplitudes()
modas()
desvios_padrao()

