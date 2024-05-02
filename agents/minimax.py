import random
from game.game import CheckersGame
from game.evaluate import score_count, score_count_upgrade
from copy import deepcopy


class MinimaxAgent:

	def minimax(self, board, depth, maximizing_player):
		if depth == 0 or board.is_over():
			return None, score_count(board)
		best_move = None
		moves = board.get_possible_moves()
		random.shuffle(moves)
		if maximizing_player:
			max_eval = float('-inf')
			for move in moves:	
				new_board = deepcopy(board)			
				new_board.move(move)
				current_move, eval = self.minimax(new_board, depth - 1, False)
				if eval > max_eval:
					max_eval = eval
					best_move = move
			return best_move, max_eval
		else:
			min_eval = float('inf')
			for move in moves:
				new_board = deepcopy(board)
				new_board.move(move)
				current_move, eval = self.minimax(new_board, depth - 1, True)
				if eval < min_eval:
					min_eval = eval
					best_move = move
			return best_move, min_eval


	def minimax_alpha_beta(self, board, depth, maximizing_player, alpha, beta):
		if depth == 0 or board.is_over():
			return None, score_count(board)
		best_move = None
		moves = board.get_possible_moves()
		random.shuffle(moves)
		if maximizing_player:
			max_eval = float('-inf')
			for move in moves:	
				new_board = deepcopy(board)			
				new_board.move(move)
				current_move, eval = self.minimax_alpha_beta(new_board, depth - 1, False, alpha, beta)
				if eval > max_eval:
					max_eval = eval
					best_move = move
					alpha = max(alpha, max_eval)
					if beta <= alpha:
						break
			return best_move, max_eval
		else:
			min_eval = float('inf')
			for move in moves:
				new_board = deepcopy(board)
				new_board.move(move)
				current_move, eval = self.minimax(new_board, depth - 1, True)
				if eval < min_eval:
					min_eval = eval
					best_move = move
					alpha = min(beta, min_eval)
					if beta <= alpha:
						break
			return best_move, min_eval

	def minimax_alpha_beta2(self, board, depth, maximizing_player, alpha, beta):
		if depth == 0 or board.is_over():
			return None, score_count_upgrade(board)
		best_move = None
		moves = board.get_possible_moves()
		random.shuffle(moves)
		if maximizing_player:
			max_eval = float('-inf')
			for move in moves:	
				new_board = deepcopy(board)			
				new_board.move(move)
				current_move, eval = self.minimax_alpha_beta(new_board, depth - 1, False, alpha, beta)
				if eval > max_eval:
					max_eval = eval
					best_move = move
					alpha = max(alpha, max_eval)
					if beta <= alpha:
						break
			return best_move, max_eval
		else:
			min_eval = float('inf')
			for move in moves:
				new_board = deepcopy(board)
				new_board.move(move)
				current_move, eval = self.minimax(new_board, depth - 1, True)
				if eval < min_eval:
					min_eval = eval
					best_move = move
					alpha = min(beta, min_eval)
					if beta <= alpha:
						break
			return best_move, min_eval
		
		
if __name__ == '__main__':
	board = CheckersGame()
	print(score_count(board))
