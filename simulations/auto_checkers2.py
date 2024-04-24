#autocheckers agente minimax con metodo de evaluación 1 vs agente minimax con metodo de evaluación 2
from agents.minimax import MinimaxAgent
from game.game import CheckersGame

def play_game():
	game = CheckersGame()
	minimax_agent = MinimaxAgent()
	while not game.is_over():
		if game.turn == 1:
			move = minimax_agent.minimax_alpha_beta(game, 3, True)
		else:
			move = minimax_agent.minimax_alpha_beta2(game, 3, True, float('-inf'), float('inf'))
		game.move(move)
		print(game)

	print(f"Juego Terminado!!")
	print(f"Ganador: {game.get_winner()}")