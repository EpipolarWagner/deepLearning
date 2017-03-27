import numpy as np

# if __name__ == "__main__":
#     user_width = int(input("What height has the game board? "))
# if __name__ == "__main__":
#     user_height = int(input("What width has the game board? "))


def board_art(board_state,height,width):
    score_line=' ---'*width

    for i in range(height):
        tube_line=''
        print(score_line)
        for j in range(width):
            tube_line=tube_line+('| %s '% board_state[j][i])
        print(tube_line+'|')
    print(score_line)

#board(user_height,user_width)

def checker_coordinate_direction(board_state,coordinate_x,coordinate_y,direction,width,height,**option):
    coordinates=np.array([[coordinate_x,coordinate_y],[coordinate_x,coordinate_y],[coordinate_x,coordinate_y]])+direction
    #coordinates=direction
    # print(board_state[(np.flipud(np.transpose(coordinates))).tolist()])
    # print(np.array([option['x_or_o']]*3))
    # print(option['x_or_o'])
    # print((board_state[(np.flipud(np.transpose(coordinates))).tolist()]==np.array([option['x_or_o']]*3)).all())
    print(direction)
    print(np.flipud(np.transpose(coordinates)))
    try:
        if ([board_state[(np.flipud(np.transpose(coordinates))).tolist()]]==np.array([option['x_or_o']]*3)).all():
            return True
        else:
            return False
    except IndexError:
        return False 
    # if (0<coordinates[0,:]).all() and (coordinates[0,:]< width).all() and (0<coordinates[1,:]).all() and  (coordinates[1,:] < height ).all() and
    #      ([board_state[(np.flipud(np.transpose(coordinates))).tolist()]]==np.array([option['x_or_o']]*3)).all():
    #         return True

    
def checker_coordinate(board_state,coordinate_x,coordinate_y,width,height):
    x_or_o=board_state[coordinate_y][coordinate_x]
    directions=np.array([[[0, -1], [0, 0],[0,1]],
                         [[-1,0], [0, 0],[1,0]],
                         [[-1,-1], [0, 0],[1,1]],
                         [[1,-1], [0, 0],[-1,1]],
                         [[0,0],[-1,-1],[-2,-2]],
                         [[0,0],[-1,0],[-2,0]],
                         [[0,0],[-1,1,],[-2,2]],
                         [[0,0],[0,1],[0,2]],
                         [[0,0],[1,1],[2,2]],
                         [[0,0],[1,0],[2,0]],
                         [[0,0],[1,1],[2,2]],
                         [[0,0],[0,-1],[0,-2]]])
    if x_or_o==' ':
        return False
    else:
        for direction in directions:
            if checker_coordinate_direction(board_state,coordinate_x,coordinate_y,direction,width,height,x_or_o=x_or_o)==True:
                return True
    return False
    

def check_board(board_state,width,height):
    for coordinate_x in range(width):
        for coordinate_y in range(height):
            if checker_coordinate(board_state,coordinate_x,coordinate_y,width,height,x_or_o=board_state[coordinate_y][coordinate_x]) == True:
                return True
    return False

    
def user_moves(width,height):
    board_state=np.full((height, width), ' ', dtype=str)
    i=0
    while i < width*height:
        player_number=(-1) ** i
        if player_number==1:
            player='X'
        else:
            player='O'     
        input_move_string=input('Next player where is your move? ')
        input_move_split_string=input_move_string.split(',')
        x_input=int((input_move_split_string[0]).strip())-1
        y_input=int((input_move_split_string[1]).strip())-1
        board_state[y_input][x_input]
        if board_state[y_input][x_input] == ' ':
            board_state[y_input][x_input]=player
        else:
            print('Invalid move, try again!')
            i=i-1
        board_art(board_state,width,height)
        if i>=4:
            if checker_coordinate(board_state,x_input,y_input,width,height)== True:
                print('player %s won' %player) 
                break
        i=i+1
        if i>=9:
            print('draw')

user_moves(4,4)
#board_state=np.array([['X', 'O', 'O'], [' ','X', 0], [' ', ' ', 'X']])
#print(board_state)
#print(checker_coordinate(board_state,1,1,3,3))
#board_with_empty_strings(4,3)
#board_art([[' ', 'X', 'O'], [' ','O', 0], [' ', 0, 0]],3,3)
#user_moves(3,3)
#print(check_board([[1, -1, 0], [0, -1, 0], [1, 0, 0]],3,3))

# winner_is_2 =[[2, 2, 0],
#  [2, 1, 0],
#  [2, 1, 1]]
# width=5
# height=6
# winner_is_1 = [[2,2,0],
#                [1, 2, 0],
# 	       [2, 1, 0],
# 	       [2, 1, 1]]

# winner_is_also_1 = [[0, 1, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 2]]
# also_no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 0]]
# winner_diagonal=[[0,0,0,0,0],
#                  [1,2,1,2,1],
#                  [4,5,6,3,8],
#                  [1,2,3,4,4],
#                  [2,3,3,4,5],
#                  [2,2,5,3,5]]


# winner_diagonal1=[[0,0,0,0,0],
#                   [1,2,1,2,1],
#                   [4,5,6,3,8],
#                   [1,2,3,4,4],
#                   [2,3,3,4,5],
#                   [2,2,5,3,2]]         
# #test=checker_coordinate(winner_is_also_1,1,0,x_or_o= 1)
# print(winner_diagonal[2+1][3-1])
# test=check_board(winner_diagonal)
# print(test)

