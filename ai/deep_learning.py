from game.game import CheckersGame
from game.evaluate import score_count
from npdl.model import Model
from npdl.layers import Dense
from npdl.optimizers import Adam
import numpy as np

class DeepLearningAgent:
	
	def __init__(self):
		self.model = Model([
			Dense(64, activation="relu", input=32),
			Dense(64, activation="relu"),
			Dense()
		])

	def train(self, board, epochs, gamma=0.9, epsilon=0.1):
		X = []
		y = []
		for epoch in range(epochs):
			state = board
			while not state.is_over():
				possible_actions = state.get_possible_moves()
				action = self.choose_action(state, possible_actions)
				next_state = state.move(action)
				reward = score_count(next_state)
				X.append(state)
				y.append(reward)
				state = next_state
			if epoch % 1000 == 0:
				print('Epoch: ', epoch)
		X = np.array(X)
		y = np.array(y)
		self.model.fit(X, y, optimizer=Adam(), epochs=epochs)

	