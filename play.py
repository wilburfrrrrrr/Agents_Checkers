from game.game import CheckersGame
from ai.minimax_pruning import minimax
from ai.random import random_agent
import random
import time

def play():
	board = CheckersGame()
	result = None
	message = ''
	try:
		while not board.game_over():
			if board.turn == 'W':
				move = minimax(board, 3, True, -float('inf'), float('inf'))
			else:
				move = random_agent(board)
			# player_name = current_player(board.turn)
			board.push_move(move[0], move[1])
			board.draw_board()
			print(board.turn, move)
			print(board.board)
			print()
			time.sleep(1)
			board.set_turn()
		print('Game Over')
		print(board.board)
		print(board.white_pieces, board.black_pieces)
	except KeyboardInterrupt:
		print('Juego Interrumpido')

	result = board.winner()
	if result == 'D':
		message = 'Empate'
	elif result == 'W':
		message = 'Ganaron las Blancas!!!'
	else:
		message = 'Ganaron las Negras!!!'

if __name__ == '__main__':
	play()