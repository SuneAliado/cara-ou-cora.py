import random

def run():
	def nicknames():
		nick1 = input('Qual o nickname do jogador 1?\n')
		nick2 = input('Qual o nickname do jogador 2?\n')

		confirm = input('Os jogadores são:\n Player1: ' + nick1 + '\n Player2: ' + nick2 + '\nIsso está certo?<s/n>\n')

		if confirm.lower() == 'n':
			return nicknames()
		elif confirm.lower() == 's':
			return(nick1, nick2)
	nick1, nick2 = nicknames()
	n1points = 0
	n2points = 0
	players = [nick1, nick2]
	choosing_player = random.choice(players)
	def game_p1():
		nonlocal n1points
		nonlocal n2points
		coin = ['cara', 'coroa']
		choosing = input('O jogador ' + nick1 + ' deve escolher (C)ara ou (K)oroa<c/k>\n')
		if choosing.lower() == 'c':
			choice = input('Você escolheu (C)ara. Tem certeza?<s/n>\n')
			if choice.lower() == 's':
				result = random.choice(coin)
				print('O resultado foi: ' + result)
				if result == 'cara':
					print('Parabéns, ' + nick1 + '! Você acertou.')
					n1points += 1
				if result == 'coroa':
					print(nick1 + ' errou.')
					n2points += 1
		if choosing.lower() == 'k':
			choice = input('Você escolheu (K)oroa. Tem certeza?<s/n>\n')
			if choice.lower() == 's':
				result = random.choice(coin)
				print('o resultado foi: ' + result)
				if result == 'coroa':
					print('Parabéns, ' + nick1 + '! Você acertou.')
					n1points += 1
				if result == 'cara':
					print(nick1 + ' errou.')
					n2points += 1
		print('A pontuação de ' + nick1 + ' é ' + str(n1points))
		print('A pontuação de ' + nick2 + ' é ' + str(n2points))
		return(n1points, n2points)
	def game_p2():
		nonlocal n1points
		nonlocal n2points
		coin = ['cara', 'coroa']
		choosing = input('O jogador ' + nick2 + ' deve escolher (C)ara ou (K)oroa<c/k>\n')
		if choosing.lower() == 'c':
			choice = input('Você escolheu (C)ara. Tem certeza?<s/n>\n')
			if choice.lower() == 's':
				result = random.choice(coin)
				print('O resultado foi: ' + result)
				if result == 'cara':
					print('Parabéns, ' + nick2 + '! Você acertou.')
					n2points += 1
				if result == 'coroa':
					print(nick2 + ' errou.')
					n1points += 1
		if choosing.lower() == 'k':
			choice = input('Você escolheu (K)oroa. Tem certeza?<s/n>\n')
			if choice.lower() == 's':
				result = random.choice(coin)
				print('o resultado foi: ' + result)
				if result == 'coroa':
					print('Parabéns, ' + nick2 + '! Você acertou.')
					n2points += 1
				if result == 'cara':
					print(nick2 + ' errou.')
					n1points += 1
		print('A pontuação de: ' + nick1 + ' é ' + str(n1points))
		print('A pontuação de: ' + nick2 + ' é ' + str(n2points))
		return(n1points, n2points)
	if(choosing_player == nick1):
		game_p1()
	if(choosing_player == nick2):
		game_p2()

	continuing = 0
	def play_again():
		nonlocal continuing
		continuing = continuing +1
		again = input('Jogar novamente?<s/n>')
		if again.lower() == 's':
			run()
		if again.lower() == 'n':
			return(continuing)
	while continuing == 0:
		play_again()
run()
