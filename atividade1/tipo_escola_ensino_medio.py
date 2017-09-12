#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

from estatisticas import *

def medias():
	media_todo_escola_publica = media_de_dado(todo_escola_publica)
	print("\nMédia de ensino médio todo em escola pública: ",
		media_todo_escola_publica)

	media_todo_escola_particular = media_de_dado(todo_escola_particular)
	print("Média de ensino médio todo em escola particular: ",
		media_todo_escola_particular)

	media_parte_escola_publica = media_de_dado(parte_escola_publica)
	print("Média de ensino médio parte em escola pública: ",
		media_parte_escola_publica)

	media_parte_escola_particular = media_de_dado(parte_escola_particular)
	print("Média de ensino médio parte em escola particular: ",
		media_parte_escola_particular)

	media_outro_tipo = media_de_dado(outro_tipo)
	print("Média de ensino médio em outro tipo de escola': ",
		media_outro_tipo)

	media_nao_respondeu = media_de_dado(nao_respondeu)
	print("Média de 'não respondeu': ",
		media_nao_respondeu)		


def medianas():
	mediana_todo_escola_publica = mediana(todo_escola_publica)
	print("\nMediana de ensino médio todo em escola pública: ",
		mediana_todo_escola_publica)

	mediana_todo_escola_particular = mediana(todo_escola_particular)
	print("Mediana de ensino médio todo em escola particular: ",
		mediana_todo_escola_particular)

	mediana_parte_escola_publica = mediana(parte_escola_publica)
	print("Mediana de ensino médio parte em escola pública: ",
		mediana_parte_escola_publica)

	mediana_parte_escola_particular = mediana(parte_escola_particular)
	print("Mediana de ensino médio parte em escola particular: ",
		mediana_parte_escola_particular)

	mediana_outro_tipo = mediana(outro_tipo)
	print("Mediana de ensino médio em outro tipo de escola': ",
		mediana_outro_tipo)

	mediana_nao_respondeu = mediana(nao_respondeu)
	print("Mediana de 'não respondeu': ",
		mediana_nao_respondeu)

def amplitudes():
	print("\nTodo em escola pública:")
	amplitude(todo_escola_publica)

	print("Todo em escola particular:")
	amplitude(todo_escola_particular)

	print("Parte em escola pública:")
	amplitude(parte_escola_publica)

	print("Parte em escola particular:")
	amplitude(parte_escola_particular)

	print("Outro tipo:")
	amplitude(outro_tipo)

	print("Não respondeu:")
	amplitude(nao_respondeu)

def modas():
	print("\nTodo em escola pública:")
	moda_dado(todo_escola_publica)

	print("Todo em escola particular:")
	moda_dado(todo_escola_particular)

	print("Parte em escola pública:")
	moda_dado(parte_escola_publica)

	print("Parte em escola particular:")
	moda_dado(parte_escola_particular)

	print("Outro tipo:")
	moda_dado(outro_tipo)

	print("Não respondeu:")
	moda_dado(nao_respondeu)	

def desvios_padrao():
	print("\nTodo em escola pública:")
	desvio_padrao(todo_escola_publica)

	print("Todo em escola particular:")
	desvio_padrao(todo_escola_particular)

	print("Parte em escola pública:")
	desvio_padrao(parte_escola_publica)

	print("Parte em escola particular:")
	desvio_padrao(parte_escola_particular)

	print("Outro tipo:")
	desvio_padrao(outro_tipo)

	print("Não respondeu:")
	desvio_padrao(nao_respondeu)

colnames =["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"]
tipo_escola_ensino_medio = pd.read_csv('fisica/FISICA-GENERO_X_TIPO_ESCOLA_ENSINO_MEDIO.csv',  names = colnames)

variaveis = tipo_escola_ensino_medio.col1[1:].tolist()
todo_escola_publica = tipo_escola_ensino_medio.col2[1:].tolist()
todo_escola_particular = tipo_escola_ensino_medio.col3[1:].tolist()
parte_escola_publica = tipo_escola_ensino_medio.col4[1:].tolist()
parte_escola_particular = tipo_escola_ensino_medio.col5[1:].tolist()
outro_tipo = tipo_escola_ensino_medio.col6[1:].tolist()
nao_respondeu = tipo_escola_ensino_medio.col7[1:].tolist()
total = tipo_escola_ensino_medio.col8[1:].tolist()

medias()
medianas()
amplitudes()
modas()
desvios_padrao()

