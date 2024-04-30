#autocheckers agente minimax vs agente random
from game.game import CheckersGame
from game.evaluate import score_count
from agents.random import RandomAgent
from agents.minimax import MinimaxAgent
import matplotlib.pyplot as plt

winners = {}

def plot_winners():
	plt.plot(winners.keys(), winners.values(), color='green', marker='o', linestyle='solid', linewidth=2, markersize=12)
	plt.title('Victorias de autocheckers')	
	plt.xlabel('Juegos')
	plt.ylabel('Ganador') 
	plt.show()

def play_game():
	game = CheckersGame()
	random_agent = RandomAgent()
	minimax_agent = MinimaxAgent()
	turn = 0
	while not game.is_over():
		turn += 1
		print(f"Número de turno: {turn}")
		if game.whose_turn() == 1:
			move, _ = minimax_agent.minimax(game, 5, True)
			# move = minimax_agent.minimax_alpha_beta(game, 3, True, -float('inf'), float('inf'))
		else:
			move = random_agent.random_agent(game)
		print(f"Jugador {game.whose_turn()} mueve: {move}")
		game.move(move)
		print(f"Puntaje: {score_count(game)}")
	winner = game.get_winner()
	final_score = score_count(game)
	print(f"Juego Terminado!!")
	print(f"Ganador: {winner}")
	print(f"Puntaje final: {final_score}")
	return winner, final_score

def play_games(number_of_games = 32):
	for game in range(number_of_games):
		print(f"\nJuego {game}")
		winner, final_score = play_game()
		if winner == 1:
			winners[game] = "Minimax"
		elif winner == 2:
			winners[game] = "Random"
		else:
			winners[game] = "Empate"

if __name__ == '__main__':
	# play_game()
	play_games()
	plot_winners()	