import numpy as np
from game.evaluate import score_count


class QLearningAgent:
	def __init__(self, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
		self.q_table = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.epsilon = epsilon

	def get_q_value(self, state, action):
		if state not in self.q_table:
			self.q_table[state] = np.zeros(len(action))
		return self.q_table[state]
	
	def update_q_value(self, state, action, reward, next_state):
		q_value = self.get_q_value(state, action)
		next_q_value = self.get_q_value(next_state)
		q_value[action] += self.learning_rate * (reward + self.discount_factor * np.max(next_q_value) - q_value[action])

	def choose_action(self, state, possible_actions):
		if np.random.uniform(0, 1) < self.epsilon:
			return np.random.choice(possible_actions)
		else:
			q_values = [self.get_q_value(state, action) for action in possible_actions]
			max_q_value = np.max(q_values)
			best_actions = [action for action, q_value in zip(possible_actions, q_values) if q_value == max_q_value]
			return np.random.choice(best_actions)


	def q_learning(self, board, episodes):
		for episode in range(episodes):
			state = board
			while not state.is_over():
				possible_actions = state.get_possible_moves()
				action = self.choose_action(state, possible_actions)
				next_state = state.move(action)
				reward = score_count(next_state)
				self.update_q_value(state, action, reward, next_state)
				state = next_state
			if episode % 1000 == 0:
				print('Episode: ', episode)

if __name__ == '__main__':
	pass