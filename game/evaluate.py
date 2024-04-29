# from game import CheckersGame

def score_count(board):
	white_score = sum([10 for piece in board.board.pieces if piece.player == 1 and not piece.captured])
	red_score = sum([10 for piece in board.board.pieces if piece.player == 2 and not piece.captured])

	white_score += sum([20 for piece in board.board.pieces if piece.player == 1 and piece.king])
	red_score += sum([20 for piece in board.board.pieces if piece.player == 2 and piece.king])

	return white_score - red_score


def cohesive_score(board):
	white_positions = [piece.position for piece in board.board.pieces if piece.player == 1]
	red_positions = [piece.position for piece in board.board.pieces if piece.player == 2]

	white_score = sum([5 for adjacent in white_positions for piece in white_positions if adjacent in [piece + 4, piece - 4, piece + 5, piece - 5]])
	red_score = sum([5 for adjacent in red_positions for piece in red_positions if adjacent in [piece + 4, piece - 4, piece + 5, piece - 5]])

	return white_score - red_score

def score_count_upgrade(board):
	score = score_count(board)
	white_score = sum([5 for piece in board.board.pieces if piece.player == 1 and piece.position in [14, 15, 18, 19]])
	red_score = sum([5 for piece in board.board.pieces if piece.player == 2 and piece.position in [14, 15, 18, 19]])

	white_score += sum([5 for piece in board.board.pieces if piece.player == 1 and piece.position in range(21, 19)])
	red_score += sum([5 for piece in board.board.pieces if piece.player == 2 and piece.position in range(5, 13)])
	cohesive_score = cohesive_score(board)

	return score + cohesive_score + white_score - red_score



# if __name__ == "__main__":
	# board = CheckersGame()
	# print(score_count(board))