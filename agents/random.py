import random
from game.game import CheckersGame

class RandomAgent:
	
	def __init__(self):
		pass

	def random_agent(self, board):
		while True:
			moves = board.get_possible_moves()
			if not moves:
				break
			move = random.choice(moves)
			return move

if __name__ == '__main__':
	board = CheckersGame()
	agent = RandomAgent()
	agent.random_agent(board)