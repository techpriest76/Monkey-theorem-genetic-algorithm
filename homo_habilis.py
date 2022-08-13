# "to be or not to be that is the question"
#ord = to numbers
#chr = to characters
#mutacao creep? no

import random

def gerar(N,L):
	pop = []
	while len(pop) < N:
		individuo = []
		while len(individuo) < L:
			valor = random.randint(97,123)
			if valor == 123:
				valor = 32
			individuo.append(valor)
		pop.append(individuo)
	return pop

def calc_fitness(cromossomo,frase):
	valor = 0
	pos = 0
	fitness = 0
	for i in cromossomo:
		if i == frase[pos]:
			valor +=1
		pos+=1
	fitness = float(valor/len(frase))
	return fitness

def torneio(participantes, N, frase):
	ganhadores = []
	while len(ganhadores) < N:

		concursantes = []
		fitness_concursantes = []

		pos1 = random.randint(0,N-1)
		pos2 = random.randint(0,N-1)

		concursantes.append(participantes[pos1])
		concursantes.append(participantes[pos2])

		for i in concursantes:
			fitness_concursantes.append(calc_fitness(i,frase))

		indice = fitness_concursantes.index(max(fitness_concursantes))
		ganhadores.append(concursantes[indice])
	
	return ganhadores

def recombinar(participantes, pc):
	recombinados = []
	for i in participantes:
		probabilidade = random.random()
		if probabilidade <= pc:
			filho=[]
			pai =  participantes[random.randint(0,len(participantes)-1)]
			k = random.randint(0,len(participantes[0])-1)
			filho[0:k] = i[0:k]
			filho[k:len(i)] = pai[k:len(i)]
			recombinados.append(filho)
		else:
			recombinados.append(i)
	return recombinados

def mutar (participantes,pm):
	mutados = []
	for i in participantes:
		for j in range(len(i)):
			probabilidade = random.random()
			if probabilidade <= pm:
				gene = random.randint(97,123)
				if gene == 123:
					gene = 32
				i[j] = gene
		mutados.append(i)
	return mutados

def melhor(participantes,frase):
	melhor = calc_fitness(participantes[0],frase)
	indice = 0
	for i in range(len(participantes)):
		if calc_fitness(participantes[i],frase) > melhor:
			melhor = calc_fitness(participantes[i],frase)
			indice = i
	return(participantes[indice],melhor)

def traduzir(palabra):
	palabra2 = []
	for i in palabra:
		valor = chr(i)
		palabra2.append(valor)
	return ''.join(palabra2)

###################################################################################################
###################################################################################################
########                                                   ########################################
########               LOOP PRINCIPAL E PARAMETROS         ########################################
########                                                   ########################################
###################################################################################################

frase_alvo = "to be or not to be that is the question"
frase = []
for i in frase_alvo:
	valor = ord(i)
	frase.append(valor)
print(frase)
print('')
L = len(frase_alvo)
N = 222
pc = 0.8
pm = 1/L
semente = 1729
rodada = 0

melhores = []
melhores_fit = []

while rodada <10:
	print('rodada: ', str(rodada+1))
	random.seed(semente)
	geracao = 0
	populacao = gerar(N,L)
	while geracao < 500:	#aumentar geracoes se nao acharem-se boas solucoes
		ganhadores = torneio(populacao,N,frase)
		recombinados = recombinar(ganhadores,pc)
		mutados = mutar(recombinados,pm)
		populacao = mutados
		best = melhor(populacao,frase)
		print(traduzir(best[0]), '------',' geracao:', str(geracao+1), '------','fitness: ', str(calc_fitness(best[0],frase)))

		if best[1] == 1:
			break

		geracao+=1
	melhores.append(best[0])
	melhores_fit.append(best[1])
	rodada+=1

	semente+=1
	print('')

print('################ Melhor de cada rodada #####################')
print('')
for i in range(len(melhores)):
	print(traduzir(melhores[i]),'----',melhores_fit[i])
