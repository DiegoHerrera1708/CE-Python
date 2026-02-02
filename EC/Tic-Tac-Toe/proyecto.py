from random import randrange


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print(f'''+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    resp = int(input("Introduce tu movimiento: "))
    salir= False
    while not salir:
        for filas in range(len(board)):
            for columnas in range(len(board[filas])):
                if resp == board[filas][columnas] and resp < 10 and resp > 0:
                    board[filas][columnas] = "O"
                    salir = True
                    break
            if salir:
                break
        else:
            print("Movimiento erróneo")
    make_list_of_free_fields(board)
    victory_for(board, "O")

    

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    global lista, fin
    lista = []
    lista_coordenadas = []
    for filas in range(len(board)):
        for columnas in range(len(board[filas])):
            if type(board[filas][columnas]) == int :
                tupla= (filas, columnas)
                lista_coordenadas.append(tupla)
    for i in range(len(lista_coordenadas)):
        lista.append(board[lista_coordenadas[i][0]][lista_coordenadas[i][1]])
    

        

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global fin, lista
    salir = False
    for filas in board:
        contador = 0
        for columnas in filas:
            if columnas == sign:
                contador += 1
            if contador == 3 and sign == "O":
                print("¡Has Ganado!")
                display_board(board)
                salir = True
                break
            if contador == 3 and sign == "X":
                print("¡Has perdido!")
                salir = True
                break
        if salir:
            fin = True
            break
    else:
        if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign) or (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
            print("¡Has perdido!")
            fin = True
    
    if len(lista) == 0:
        print("Empate")
        fin = True

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    salir = False
    random = randrange(len(lista))
    maquina = lista[random]
    for filas in range(len(board)):
        for columnas in range(len(board[filas])):
            if board[filas][columnas] == maquina:
                board[filas][columnas] = "X"
                salir = True
                break
        if salir:
            break

    print("Movimiento de la maquina")
    display_board(board)
    make_list_of_free_fields(board)
    victory_for(board, "X")


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
lista=[]
fin = False
display_board(board)

while not fin:
    enter_move(board)
    if fin:
        break
    make_list_of_free_fields(board)
    draw_move(board)

