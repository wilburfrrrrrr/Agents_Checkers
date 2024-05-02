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

	def encode_state(self, board):
		state = np.zeros((1, 33))
		for piece in board.board.pieces:
			if piece.player == 1 and not piece.captured:
				state[0][piece.position] = 1 if not piece.king else 5
			elif piece.player == 2 and not piece.captured:
				state[0][piece.position] = -1 if not piece.king else -5
		return state

	def encode_action(self, action):
		return np.array(action)

	def decode_action(self, action):
		return action

	def train(self, board, epochs=50):
		model = self.model
		for _ in range(epochs):
			player_1 = MinimaxAgent()
			player_2 = MinimaxAgent()
			state = deepcopy(board)
			while not state.is_over():
				next_state = deepcopy(state)
				if state.whose_turn() == 1:
					action, _ = player_1.minimax_alpha_beta2(next_state, 4, True, -float('inf'), float('inf'))
				else:
					action, _ = player_2.minimax_alpha_beta2(next_state, 4, False, -float('inf'), float('inf'))
				next_state.move(action)
				print(f"action: {action}")
				encoded_state = self.encode_state(state)
				encoded_action = self.encode_action(action)
				print(f"encoded action: {encoded_action}")
				model.fit(encoded_state, encoded_action)
				state = next_state

	def select_move(self, board):
		move = self.model.predict(self.encode_state(board))
		print(f"action: {move}")
		return self.decode_action(move)
				
if __name__ == "__main__":
	game = CheckersGame()
	deep_learning_agent = DeepLearningAgent(game)
	deep_learning_agent.compile()
	deep_learning_agent.train(game)
	print("Training complete!")

	