import turtle
from game import CheckersGame


def draw_board(game):
	turtle.speed(0)
	turtle.hideturtle()
	turtle.pu()
	turtle.goto(-200, 200)
	turtle.pd()
	turtle.color('black')
	for _ in range(8):
		for _ in range(8):
			turtle.begin_fill()
			for _ in range(4):
				turtle.forward(50)
				turtle.right(90)
			turtle.end_fill()
			turtle.forward(50)
		turtle.backward(200)
		turtle.right(90)
		turtle.forward(50)
		turtle.left(90)
	for row in range(8):
		for col in range(8):
			if board.get_piece(row, col) == 'W':
				turtle.goto(col * 50 - 200 + 25, 200 - row * 50 - 25)
				turtle.begin_fill()
				turtle.color('white')
				turtle.circle(25)
				turtle.end_fill()
			elif board.get_piece(row, col) == 'WK':
				turtle.goto(col * 50 - 200 + 25, 200 - row * 50 - 25)
				turtle.begin_fill()
				turtle.color('white')
				turtle.circle(25)
				turtle.end_fill()
				turtle.color('black')
				turtle.write('K', align='center', font=('Arial', 12, 'normal'))
			elif board.get_piece(row, col) == 'B':
				turtle.goto(col * 50 - 200 + 25, 200 - row * 50 - 25)
				turtle.begin_fill()
				turtle.color('black')
				turtle.circle(25)
				turtle.end_fill()
			elif board.get_piece(row, col) == 'BK':
				turtle.goto(col * 50 - 200 + 25, 200 - row * 50 - 25)
				turtle.begin_fill()
				turtle.color('black')
				turtle.circle(25)
				turtle.end_fill()
				turtle.color('white')
				turtle.write('K', align='center', font=('Arial', 12, 'normal'))


if __name__ == '__main__':
	board = CheckersGame()
	draw_board(board)
	turtle.done()