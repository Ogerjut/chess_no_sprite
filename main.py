# faire un array pour modéliser échiquier

from array import *
board = array("i", [11,13,15,17,18,16,14,12,
                    10,10,10,10,10,10,10,10,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,
                    1,1,1,1,1,1,1,1,
                    2,4,6,8,9,7,5,3])

# pas pièces dans le array
step_pawnw = - 8
step_pawnb = 8 

# opération sur le array pour bouger pièces  

def print_board():
    list_piece = []
    for val in range (len(board)):
        list_piece.append(board[val])
        if len(list_piece) == 8 :
            print(list_piece)
            list_piece.clear()
        
def get_busy():
    for val in range (len(board)):
        if board[val] == 0 :
            return False
        
def get_piece(val):
    return board[val]
            
def move(current_pos, new_pos, piece):
    for val in range (len(board)):
        if val == current_pos : 
            board[val] = 0
        if val == new_pos : 
            board[val] = piece

def authorized_move(piece, current_pos):
        list_authorized_tile = []
        if piece == 1 : 
            new_pos = current_pos + step_pawnw
            if board[new_pos] == 0 : 
                list_authorized_tile.append(new_pos)
                print(f"La case autorisée est {new_pos}")
        return list_authorized_tile
                
     
print_board()
print("\n")
# print(len(board))
# print(board.index(0, 0, len(board)))
# board[3] = 3

authorized_move(1, 48) 
# move(63, 12, 2)

print_board()



