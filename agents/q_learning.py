import random
from game.evaluate import score_count_upgrade
from agents.minimax import MinimaxAgent
from copy import deepcopy

class QLearningAgent:
	def __init__(self, learning_rate=0.1, discount_factor=0.9):
		self.q_table = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor

	def get_q_value(self, state, action):
		q_action = tuple(action)
		if state not in self.q_table:
			self.q_table[state] = {}
		if q_action not in self.q_table[state]:
			self.q_table[state][q_action] = 0
		return self.q_table[state][q_action]
	
	def update_q_value(self, state, action, reward, next_state, next_actions):
		q_value = self.get_q_value(state, action)
		next_q_value = max([self.get_q_value(next_state, next_action) for next_action in next_actions]) if next_actions else 1
		q_value += self.learning_rate * (reward + self.discount_factor * next_q_value - q_value)
		self.q_table[state][tuple(action)] = q_value

	def choose_action(self, state, possible_actions):
		q_values = [self.get_q_value(state, action) for action in possible_actions]
		max_q_value = max(q_values)
		best_actions = [action for action, q_value in zip(possible_actions, q_values) if q_value == max_q_value]
		return random.choice(best_actions)

	def get_reward(self, state):
		if state.is_over():
			if state.get_winner() == 1: return 100  
			elif state.get_winner() == 2: return -100 
			else: return 0
		return score_count_upgrade(state)
	
	def get_next_state(self, state, action):
		next_state = deepcopy(state)
		next_state.move(action)
		return next_state

	def q_learning(self, board, episodes = 100):
		for episode in range(episodes):
			player_1 = MinimaxAgent()
			player_2 = MinimaxAgent()
			state = deepcopy(board)
			while not state.is_over():
				if state.whose_turn() == 1:
					action, _ = player_1.minimax_alpha_beta2(state, 4, True, -float('inf'), float('inf'))
				else:
					action, _ = player_2.minimax_alpha_beta2(state, 4, False, -float('inf'), float('inf'))
				next_state = self.get_next_state(state, action)
				next_actions = next_state.get_possible_moves()
				reward = self.get_reward(next_state)
				self.update_q_value(state, action, reward, next_state, next_actions)
				state = next_state

if __name__ == '__main__':
	pass