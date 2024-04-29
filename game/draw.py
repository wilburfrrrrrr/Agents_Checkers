import turtle
from game import CheckersGame

def index_to_coords(index):
	row = index // 4
	col = 2*(index % 4) + ((row + 1) % 2)
	print(row, col)
	return row, col

def coords_to_index(row, col):
	return 4*row + col//2

def setup_screen():
	turtle.speed(0)
	turtle.hideturtle()
	screen = turtle.Screen()
	screen.title("Damas")
	screen.colormode(255)
	screen.bgcolor((234, 255, 221))
	screen.setup(width=600, height=600)
	return screen

def draw_board():
	for i in range(8):
		for j in range(8):
			if (i + j) % 2 == 0:
				turtle.begin_fill()
				turtle.penup()
				turtle.fillcolor((128, 81, 40))
				turtle.goto(-300 + 75 * i, 300 - 75 * j)
				turtle.pendown()
				for _ in range(4):
					turtle.forward(75)
					turtle.right(90)
				turtle.end_fill()
			else:
				turtle.begin_fill()
				turtle.penup()
				turtle.fillcolor((247, 255, 221))
				turtle.goto(-300 + 75 * i, 300 - 75 * j)
				turtle.pendown()
				for _ in range(4):
					turtle.forward(75)
					turtle.right(90)
				turtle.end_fill()

def draw_piece(x, y, color):
	turtle.penup()
	turtle.goto(y, x)
	turtle.pendown()
	turtle.begin_fill()
	turtle.fillcolor(color)
	turtle.circle(30)
	turtle.end_fill()

def update_board(board):
	for piece in board.board.pieces:
		x, y = index_to_coords(piece.position)
		x = -300 + 75 * x 
		y = 300 - 75 * y 
		if piece.player == 1:
			draw_piece(x, y, (247, 255, 221))
		else:
			draw_piece(x, y, (128, 81, 40))



		

if __name__ == '__main__':
	board = CheckersGame()
	setup_screen()
	draw_board()
	update_board(board)
	turtle.mainloop()
