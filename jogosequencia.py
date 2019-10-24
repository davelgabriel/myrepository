import os
from random import randint

def limpa():
	if os.name==("nt"):
		os.system("cls")
	else:
		os.system("clear")

def pergunta():
		resposta = input ("""Sua memoria é boa?
       
""")
		return resposta 

def jogo():
	n= randint(0,9)
	correta = str (n)
	pontos = 0
	print('''
O primeiro número é: ''',n)
	s = input("Agora digite a sequencia completa: ")
	#if s == n:
	while s == correta:
		limpa()
		n= randint(0,9)
		correta += str (n)
		print("O proximo número é:",n)
		s = input("Agora digite a sequencia completa: ")
		pontos += 1
	if pontos > 10:
				print('''!!!PARABÉNS!!! 
Sua memoria é boa mesmo!
Sua pontuação:''', pontos,'''
A sequencia correta era:''', correta)
	else:			
					print ('''!!!ERROOOOOOOOOOOOU!!!
Mas não se preocupa, dá pra melhorar!''')
					print("A sequencia correta era: ", correta)
					print("Sua pontuação:", pontos)
	#else:
		#ALGUMA FORMA DE REINICIAR O JOGO
		
def main(args):

	x = pergunta()
	limpa()
	if x == 'sim' or x  == 'Sim' or x == 'SIM' or x == 's':
	
		print('''DUVIDO!!!
		
Para você me provar o contrario, preparei um teste. 
É simples, eu irei anunciar números aleatórios e sua função é decorar o máximo possível, criando uma sequencia.

O primeiro numero é: 2
Agora digite a sequencia completa: 2

O proximo numero é: 3
Agora digite a sequencia completa: 23

ENTENDIDO?
Cada acerto somará 1 ponto, consegue atingir 10? ''')
		jogo()
	
		
	if x == 'nao' or x == 'não' or x == "NÃO" or x  == "NAO" or x == 'n':
		print('''Ok, vou perguntar de novo, mas dessa vez digite: SIM.
OBS: Vamos colaborar, não custa nada.
''') 
#caso ele tenha digitado não de primeira e não consiga os 10 pontos colocar: voce não é bom de memoria mesmo, venceu
		x = pergunta()
		if x == 'sim' or x  == 'Sim' or x == 'SIM' or x == 's':
			limpa()
			print('''É simples, eu irei anunciar números aleatórios e sua função é decorar o máximo possível, criando uma sequencia.

O primeiro numero é: 2
Agora digite a sequencia completa: 2

O proximo numero é: 3
Agora digite a sequencia completa: 23

ENTENDIDO?
Cada acerto somará 1 ponto, consegue atingir 10? ''')
			jogo()
		
		if x == 'nao' or x == 'não' or x == "NÃO" or x  == "NAO" or x == 'n':
			limpa()
			print("VENCEU")		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
