#coding: utf-8
'''

'''

import math

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



# fim da matrizCos()


def main():
	vetR = {};
	vetS = {};

	vetR['x'] = 1;
	vetR['y'] = 2;
	vetR['z'] = 3;

	vetS['x'] = 5;
	vetS['y'] = 6;
	vetS['z'] = 1;

	print(cosseno(vetR,vetS))

	return 0
# def main

if __name__ == "__main__":
    main()