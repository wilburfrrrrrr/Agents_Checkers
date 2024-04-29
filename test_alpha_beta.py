import matplotlib.pyplot as plt
from copy import deepcopy
from game.game import CheckersGame
from agents.minimax import MinimaxAgent
import time

minimax_depths = {}

def plot_minimax():
	plt.plot(minimax_depths.keys(), minimax_depths.values(), color='blue', marker='o', linestyle='solid', linewidth=2, markersize=12)
	plt.xlabel('Depth')
	plt.ylabel('Time')
	plt.title('Minimax Depth vs Time')
	plt.show()


def test_minimax(depths = 7):
	board = CheckersGame()
	agent = MinimaxAgent()
	for depth in range(1, depths + 1):
		new_board = deepcopy(board)
		start = time.time()
		agent.minimax_alpha_beta(new_board, depth, True, -float('inf'), float('inf'))
		end = time.time()
		minimax_depths[depth] = end - start

if __name__ == '__main__':
	test_minimax()
	plot_minimax()