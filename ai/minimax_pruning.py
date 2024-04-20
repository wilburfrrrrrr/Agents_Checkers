import random
from game.game import CheckersGame
from game.evaluate import score_count
# from game.board import CheckerBoard

#bpard = CheckerBoard()

# def score_count(board):
# 	white_score = 0
# 	black_score = 0
# 	for piece in board.board.pieces:
# 		if piece.player == 1:
# 			white_score += 1
# 		elif piece.player == 2:
# 			black_score += 1
# 		if piece.king:
# 			if piece.player == 1:
# 				white_score += 2
# 			elif piece.player == 2:
# 				black_score += 2
# 	return white_score - black_score


def minimax(board, depth, maximizing_player, alpha, beta):
	if depth == 0 or board.is_over():
		return score_count(board)
	moves = random.shuffle(board.possible_moves())
	if maximizing_player:
		max_eval = float('-inf')
		for move in moves:
			board.move(move[0], move[1])
			eval = minimax(board, depth - 1, False, alpha, beta)
			board.pop_move()
			max_eval = max(max_eval, eval)
			alpha = max(alpha, eval)
			if beta <= alpha:
				break
		return max_eval
	else:
		min_eval = float('inf')
		for move in board.legal_moves():
			board.push_move(move[0], move[1])
			eval = minimax(board, depth - 1, True, alpha, beta)
			board.pop_move()
			min_eval = min(min_eval, eval)
			beta = min(beta, eval)
			if beta <= alpha:
				break
		return min_eval

def play():
	pass

def main():
	pass

if __name__ == '__main__':
	board = CheckersGame()
	print(score_count(board))
