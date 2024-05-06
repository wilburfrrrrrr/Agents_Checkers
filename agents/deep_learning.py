from game.game import CheckersGame
from npdl.model import Model
from npdl.layers import Dense
from npdl.optimizers import Adam
import numpy as np
from agents.minimax import MinimaxAgent
from copy import deepcopy

class DeepLearningAgent:
	
	def __init__(self):
		# self.board = board
		self.model = Model([
			Dense(192, activation="relu", n_in=32),
			Dense(192, activation="relu"),
			Dense(192, activation="relu"),
			Dense(192, activation="relu"),
			Dense(192, activation="relu"),
			Dense(1, activation="softmax")
		])

	def compile(self):
		self.model.compile(optimizer=Adam(), loss="mse")

	def encode_state(self, state):
		return np.array(state, dtype=int)

	def encode_action(self, action):
		return np.array(action, dtype=int)

	def decode_action(self, action):
		return action.to_list()

	def train(self, board, epochs=100):
		model = self.model
		for _ in range(epochs):
			player_1 = MinimaxAgent()
			player_2 = MinimaxAgent()
			new_board = deepcopy(board)
			while not new_board.is_over():
				state = board.get_possible_moves()
				if new_board.whose_turn() == 1:
					action, _ = player_1.minimax_alpha_beta2(new_board, 4, True, -float('inf'), float('inf'))
				else:
					action, _ = player_2.minimax_alpha_beta2(new_board, 4, False, -float('inf'), float('inf'))
				encoded_state = self.encode_state(state)
				encoded_action = self.encode_action(action)
				model.fit(encoded_state, encoded_action)
				board.move(action)

	def select_move(self, possible_moves):
		move = self.model.predict(self.encode_state(possible_moves))
		return self.decode_action(move)
				
if __name__ == "__main__":
	game = CheckersGame()
	deep_learning_agent = DeepLearningAgent(game)
	deep_learning_agent.compile()
	deep_learning_agent.train(game)
	print("Training complete!")

	