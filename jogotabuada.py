import os
from random import randint

def correta(z):
	print()
	print("OOPS!")
	print("A resposta certa é", z)
	print("Não se preocupe, só estudar mais!")
	
def limpa():
	if os.name==("nt"):
		os.system("cls")
	else:
		os.system("clear")

def main(args):
	print("Vamos ver se você é bom de tabuada: ")
	i=1
	print("NIVEL",i)
	x = randint(0,5)
	y = randint(0,5)
	z = x*y
	print("Qual a resposta correta da multiplicação?")
	resposta=int(input("{} x {} = ".format(x,y)))
	cont=0
	
	if resposta == z:
		limpa()
		while resposta == z and cont<2:
				i=1
				print("NIVEL",i)
				x = randint(0,5)
				y = randint(0,5)
				z = x*y
				print("Qual a resposta correta da multiplicação?")
				resposta=int(input("{} x {} = ".format(x,y)))
				limpa()
				cont+=1
	if cont > 2:
		while resposta == z:
			i=2
			print("NIVEL",i)
			x = randint(0,5)
			y = randint(0,5)
			z = x*y
			print("Qual a resposta correta da multiplicação?")
			resposta=int(input("{} x {} = ".format(x,y)))
			limpa()
			cont+=1
	else:
		correta(z)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
