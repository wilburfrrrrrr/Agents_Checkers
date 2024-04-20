from game import CheckersGame

def score_count(board):
	white_score = 0
	black_score = 0
	for piece in board.board.pieces:
		if piece.player == 1:
			white_score += 1
		elif piece.player == 2:
			black_score += 1
		if piece.king:
			if piece.player == 1:
				white_score += 2
			elif piece.player == 2:
				black_score += 2
	return white_score - black_score


def score_count_upgrade(board):
	first_score = score_count(board)

if __name__ == "__main__":
	board = CheckersGame()
	print(score_count(board))