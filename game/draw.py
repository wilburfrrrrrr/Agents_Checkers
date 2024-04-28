import turtle
from game import CheckersGame

turtle.tracer(0, 0)

def index_to_coords(index):
    row = (index - 1) // 4
    col = ((index - 1) % 4) * 2 + 1 if row % 2 == 0 else ((index - 1) % 4) * 2
    
    print(f"Índice: {index}, Coordenadas: ({row}, {col})")
    return row, col


def coords_to_index(row, col):
    if row % 2 == 0:
        return 4 * row + col // 2 + 1
    else:
        return 4 * row + (col + 1) // 2 + 1

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
				turtle.fillcolor((247, 255, 221))
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
				turtle.fillcolor((128, 81, 40))
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
		x = -300 + 75 * x +8
		y = 300 - 75 * y -37
		if piece.player == 1:
			draw_piece(x, y, (247, 255, 221))
		else:
			draw_piece(x, y, (28, 28, 28))

selected_piece = None  # Variable para almacenar la posición de la ficha seleccionada

def on_click(x, y):
    global selected_piece
    
    # Convertir las coordenadas del clic a coordenadas del tablero
    col = 7 - int((x + 300) // 75)  # Invertir la columna
    row = int((y + 300) // 75)
    
    # Verificar si las coordenadas están dentro del tablero
    if 0 <= row < 8 and 0 <= col < 8:
        # Calcular el índice a partir de las coordenadas
        index = coords_to_index(row, col)
        
        # Obtener las piezas en el tablero
        pieces = board.board.pieces
        
        # Verificar si hay una pieza en la casilla seleccionada
        clicked_piece = None
        for piece in pieces:
            if piece.position == index:
                clicked_piece = piece
                break
        
        # Si se ha seleccionado una pieza válida
        if clicked_piece is not None:
            # Si hay una pieza previamente seleccionada, restaura su color original
            if selected_piece is not None:
                x_prev, y_prev = index_to_coords(selected_piece.position)
                x_prev = -300 + 75 * x_prev + 8
                y_prev = 300 - 75 * y_prev - 37
                if selected_piece.player == 1:
                    draw_piece(x_prev, y_prev, (247, 255, 221))  # Color normal para jugador 1
                else:
                    draw_piece(x_prev, y_prev, (28, 28, 28))  # Color normal para jugador 2
            
            # Resalta la nueva ficha seleccionada
            x, y = index_to_coords(index)
            x = -300 + 75 * x + 8
            y = 300 - 75 * y - 37
            draw_piece(x, y, (135, 206, 235))  # Azul claro
            
            # Actualiza la ficha seleccionada
            selected_piece = clicked_piece
        else:
            print("No hay una ficha en esa casilla")
    else:
        print("Clic fuera del tablero")

		

if __name__ == '__main__':
	board = CheckersGame()
	setup_screen()
	draw_board()
	update_board(board)
	turtle.onscreenclick(on_click)



turtle.update()
turtle.mainloop()	
