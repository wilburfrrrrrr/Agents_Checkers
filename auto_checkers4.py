#autocheckers agente d learning vs agente minimax

#autocheckers agente q learning vs agente minimax
from game.game import CheckersGame
from game.evaluate import score_count_upgrade
from agents.deep_learning import DeepLearningAgent
from agents.minimax import MinimaxAgent
import matplotlib.pyplot as plt

winners = {}

def get_deep_learning_agent():
	print("Entrenando agente Deep Learning...")
	deep_learning = DeepLearningAgent()
	deep_learning.compile()
	deep_learning.train(CheckersGame())
	return deep_learning

def plot_winners():
	plt.plot(winners.keys(), winners.values(), color='green', marker='o', linestyle='solid', linewidth=2, markersize=12)
	plt.title('Victorias de autocheckers')	
	plt.xlabel('Juegos')
	plt.ylabel('Ganador') 
	plt.show()

def play_game(player_1, player_2):
	game = CheckersGame()
	turn = 0
	while not game.is_over():
		turn += 1
		print(f"Número de turno: {turn}")
		if game.whose_turn() == 1:
			move = player_1.select_move(game.get_possible_moves())
		else:
			move = player_2.minimax(game, 3, False)
		print(f"Jugador {game.whose_turn()} mueve: {move}")
		game.move(move)
		print(f"Puntaje: {score_count_upgrade(game)}")
	
	winner = game.get_winner()
	print(f"Juego Terminado!!")
	print(f"Ganador: {winner}")
	return winner

def play_games(number_of_games = 10):
	player_1 = get_deep_learning_agent()
	player_2 = MinimaxAgent().minimax_alpha_beta
	for game in range(number_of_games):
		print(f"\nJuego {game}")
		winner = play_game(player_1, player_2)
		if winner == 1:
			winners[game] = "Q Learning"
		elif winner == 2:
			winners[game] = "Minimax"
		else:
			winners[game] = "Empate"

if __name__ == '__main__':
	play_games()
	plot_winners()