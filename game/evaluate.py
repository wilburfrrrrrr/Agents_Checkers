# from game import CheckersGame

def score_count(board):
	white_score = sum([10 for piece in board.board.pieces if piece.player == 1 and not piece.captured])
	red_score = sum([10 for piece in board.board.pieces if piece.player == 2 and not piece.captured])

	return white_score - red_score

def king_score(board):
	white_score = sum([20 for piece in board.board.pieces if piece.player == 1 and piece.king])
	red_score = sum([20 for piece in board.board.pieces if piece.player == 2 and piece.king])

	return white_score - red_score

def central_score(board):
	white_score = sum([5 for piece in board.board.pieces if piece.player == 1 and piece.position in [14, 15, 18, 19]])
	red_score = sum([5 for piece in board.board.pieces if piece.player == 2 and piece.position in [14, 15, 18, 19]])
	
	return white_score - red_score

def score_count_upgrade(board):
	score = score_count(board)
	score += king_score(board)
	score += central_score(board)

	return score

	# white_score += sum([5 for piece in board.board.pieces if piece.player == 1 and piece.position in range(21, 29)])
	# red_score += sum([5 for piece in board.board.pieces if piece.player == 2 and piece.position in range(5, 13)])
	# # score += cohesive_score(board)

	# return score + white_score - red_score



# if __name__ == "__main__":
	# board = CheckersGame()
	# print(score_count(board))