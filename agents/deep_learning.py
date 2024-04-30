from game.game import CheckersGame
from game.evaluate import score_count
from npdl.model import Model
from npdl.layers import Dense
from npdl.optimizers import Adam
import numpy as np
from minimax import MinimaxAgent
from q_learning import QLearningAgent
from copy import deepcopy

class DeepLearningAgent:
	
	def __init__(self, board):
		self.board = board
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

	def train(self,board, epochs=50):
		model = self.model
		for _ in range(epochs):
			player_1 = MinimaxAgent()
			player_2 = MinimaxAgent()
			state = deepcopy(board)
			while not state.is_over():
				next_state = deepcopy(state)
				if state.whose_turn() == 1:
					action, _ = player_1.minimax_alpha_beta(next_state, 4, True, -float('inf'), float('inf'))
				else:
					action = player_2.minimax_alpha_beta(next_state, 4, False, -float('inf'), float('inf'))
				model.fit(state, action)
				state = next_state

	def select_move(self, board):
		pass
				


	

	