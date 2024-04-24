from game.game import CheckersGame
from game.evaluate import score_count
from npdl.model import Model
from npdl.layers import Dense
from npdl.optimizers import Adam
import numpy as np

class DeepLearningAgent:
	
	def __init__(self, board):
		self.board = board
		self.model = Model([
			Dense(64, activation="softmax", n_in=32),
			Dense(64, activation="softmax"),
			Dense(192, activation="linear")
		])

	def compile(self):
		self.model.compile(optimizer=Adam(), loss="mse")

	def get_reward(self, state):
		return score_count(state)
	
	def encode_state(self):
		state = self.board()

	def best_move(self, value, actions):
		best_value = -1
		best_action = None
		for action in actions:
			new_value = value[action]
			if new_value > best_value:
				best_value = new_value
				best_action = action
		return best_action
		
	def train(self, epochs=1000):
		for i in range(epochs):
			current_state = CheckersGame()
			
			while not current_state.is_over():
				actions = current_state.get_possible_moves()
				values = []
				action = self.best_move(values, actions)
				next_state = current_state.move(action)
				reward = self.get_reward(next_state)
				#agent.update(state, action, reward, next_state, done)??? // model.fit(state, reward)???
				current_state = next_state


				


	

	