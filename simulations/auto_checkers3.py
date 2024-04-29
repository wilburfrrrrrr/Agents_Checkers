#autocheckers agente q learning vs agente minimax
from agents.q_learning import QLearningAgent
from agents.minimax import MinimaxAgent
from agents.random import RandomAgent
from game.game import CheckersGame

def play_game():
	game = CheckersGame
	q_learning_agent = QLearningAgent
	minimax_agent = MinimaxAgent
	random_agent = RandomAgent
	while not game.is_over():
		if game.whose_turn() == 1:
			move = q_learning_agent.q_learning
