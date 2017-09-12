#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

from estatisticas import *

def medias():
	media_zona_urbana = media_de_dado(zona_urbana)
	print("\nMédia de moradia em zona urbana: ",
		media_zona_urbana)

	media_zona_rural = media_de_dado(zona_rural)
	print("Média de moradia em zona rural: ",
		media_zona_rural)

	media_nao_se_aplica = media_de_dado(nao_se_aplica)
	print("Média de 'não se aplica': ",
		media_nao_se_aplica)		


def medianas():
	mediana_zona_urbana = mediana(zona_urbana)
	print("\nMediana de moradia em zona urbana: ",
		mediana_zona_urbana)

	mediana_zona_rural = mediana(zona_rural)
	print("Mediana de moradia em zona rural: ",
		mediana_zona_rural)

	mediana_nao_se_aplica = mediana(nao_se_aplica)
	print("Mediana de 'não se aplica': ",
		mediana_nao_se_aplica)

def amplitudes():
	print("\nZona urbana:")
	amplitude(zona_urbana)

	print("Zona rural:")
	amplitude(zona_rural)

	print("Não se aplica:")
	amplitude(nao_se_aplica)

def modas():
	print("\nZona urbana:")
	moda_dado(zona_urbana)

	print("Zona rural:")
	moda_dado(zona_rural)

	print("Não se aplica:")
	moda_dado(nao_se_aplica)	

def desvios_padrao():
	print("\nZona urbana:")
	desvio_padrao(zona_urbana)

	print("Zona rural:")
	desvio_padrao(zona_rural)

	print("Não se aplica:")
	desvio_padrao(nao_se_aplica)

colnames =["col1", "col2", "col3", "col4", "col5"]
local_moradia = pd.read_csv('fisica/FISICA-GENERO_X_LOCAL_DE_MORADIA.csv',  names = colnames)

variaveis = local_moradia.col1[1:].tolist()
zona_urbana = local_moradia.col2[1:].tolist()
zona_rural = local_moradia.col3[1:].tolist()
nao_se_aplica = local_moradia.col4[1:].tolist()
total = local_moradia.col5[1:].tolist()

medias()
medianas()
amplitudes()
modas()
desvios_padrao()

