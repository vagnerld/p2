#coding: utf-8
'''

'''

import math
import random

# define o cosseno entre dois vetores
def cosseno(lstU, lstV):
	sum1 = 0
	sumU = 0
	sumV = 0
	if(len(lstU)==len(lstV)):
		for (key, title) in lstU.items(): # somatorio Ui*Vi
			sum1 += lstU[key]*lstV[key]
		# fim for
		
		for (key, title) in lstU.items(): # somatorio Ui**2
			sumU += lstU[key]**2
		# fim for

		for (key, title) in lstU.items(): # somatorio Vi**2
			sumV += lstV[key]**2
		# fim for

		return math.degrees(math.acos(sum1/(math.sqrt(sumU) * math.sqrt(sumV)))) # resultado do angulo entre dois vetores em graus º
	else :
		return None # Os vetores não possuem a mesma quantidade de dimensões
# fim da cosseno()


def matrizCos(lstVet):

	print('legal')

# fim da matrizCos()


def geraMatriz():
	lstArq = carregaArq('./vetnotebooks/bdev.txt')

	for x in xrange(len(lstArq)):
		arq = []
		arq = carregaArq('./vetnotebooks/'+lstArq[x])
		print(arq);


# fim def geraMatriz


def carregaArq(arquivo):
    lst=[]
    arq=open(arquivo,'rt')
    
    linha=arq.readline()
    while linha!='':
        linha = linha.replace('\r\n','')
        lst.append(linha)
        linha=arq.readline()
    #fim do while
    return lst
# fim carregaArq





def main():
	vetR = {};
	vetS = {};

	vetR['x'] = 1;
	vetR['y'] = 2;
	vetR['z'] = 3;

	vetS['x'] = 5;
	vetS['y'] = 6;
	vetS['z'] = 1;
	vetvet = [[random.randint(1,9) for x in range(3)] for x in range(10)]

	
	print(cosseno(vetR,vetS))
	print(geraMatriz())

	return 0
# def main

if __name__ == "__main__":
    main()