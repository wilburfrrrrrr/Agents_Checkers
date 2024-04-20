import random
from game.game import CheckersGame

def random_agent(board):
	while True:
		moves = board.get_possible_moves()
		if not moves:
			break
		move = random.choice(moves)
		return move

if __name__ == '__main__':
	board = CheckersGame()
	random_agent(board)