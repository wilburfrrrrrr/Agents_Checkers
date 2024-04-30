#autocheckers agente minimax con metodo de evaluación 1 vs agente minimax con metodo de evaluación 2
from agents.minimax import MinimaxAgent
from game.game import CheckersGame
from game.evaluate import score_count_upgrade
import matplotlib.pyplot as plt

winners = {}

def plot_winners():
	plt.plot(winners.keys(), winners.values(), color='red', marker='o', linestyle='solid', linewidth=2, markersize=12)
	plt.title('Victorias de autocheckers con diferentes evaluaciones')	
	plt.xlabel('Juegos')
	plt.ylabel('Ganador') 
	plt.show()

def play_game():
	game = CheckersGame()
	minimax_agent = MinimaxAgent()
	turn = 0
	while not game.is_over():
		turn += 1
		print(f"Número de turno: {turn}")
		if game.whose_turn() == 1:
			move, _ = minimax_agent.minimax_alpha_beta2(game, 5, True, float('-inf'), float('inf'))
		else:
			move, _ = minimax_agent.minimax_alpha_beta(game, 5, False, float('-inf'), float('inf'))
		print(f"Jugador {game.whose_turn()} mueve: {move}")
		game.move(move)
		print(f"Puntaje: {score_count_upgrade(game)}")

	winner = game.get_winner()	
	final_score = score_count_upgrade(game)
	print(f"Juego Terminado!!")
	print(f"Ganador: {winner}")
	print(f"Puntaje final: {final_score}")
	return winner, final_score

def play_games(number_of_games = 10):
	for game in range(number_of_games):
		print(f"\nJuego {game}")
		winner, final_score = play_game()
		if winner == 1:
			winners[game] = "Minimax con evaluación modificada"
		elif winner == 2:
			winners[game] = "Minimax con evaluación básica"
		else:
			winners[game] = "Empate"

if __name__ == '__main__':
	play_game()
	# play_games()
	# plot_winners()