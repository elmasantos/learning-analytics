#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import statistics 

def converte_para_float(dado):
	new_dado = [float(sal.replace("'", "")) for sal in dado]
	return new_dado

def media_de_dado(dado):	
	new_dado = converte_para_float(dado)
	media = statistics.mean(new_dado)
	return media

def mediana(dado):
	new_dado = converte_para_float(dado)

	n = len(new_dado)
	new_dado.sort()
	mediana = statistics.median(new_dado)
	return mediana

def moda_dado(dado):
	new_dado = converte_para_float(dado)
	try:
		moda = statistics.mode(new_dado)
	except Exception:
		moda = "Não há moda"
	print(moda)

def amplitude(dado):
	new_dado = converte_para_float(dado)
	maior = max(new_dado)
	menor = min(new_dado)
	print('\tMáximo: ', maior, '\tMínimo:', menor)
	print('\tAmplitude: ', maior - menor)

def desvio_padrao(dado):
	new_dado = converte_para_float(dado)
	dp = statistics.stdev(new_dado)
	print('\tDesvio padrão: ',dp)
