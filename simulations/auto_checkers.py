#autocheckers agente minimax vs agente random
from game.game import CheckersGame
from agents.random import RandomAgent
from agents.minimax import MinimaxAgent

def play_game():
	game = CheckersGame()
	random_agent = RandomAgent()
	minimax_agent = MinimaxAgent()
	while not game.is_over():
		if game.turn == 1:
			move = minimax_agent.minimax(game, 3, True)
			move = minimax_agent.minimax_alpha_beta(game, 3, True, -float('inf'), float('inf'))
		else:
			move = random_agent.random_agent(game)
		game.move(move)
		print(game)

	print(f"Juego Terminado!!")
	print(f"Ganador: {game.get_winner()}")

if __name__ == '__main__':
	play_game