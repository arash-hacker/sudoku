import numpy as np
from collections import Counter

board=np.array([#easy 10s 49e
    [3, 0, 6, 5, 0, 8, 4, 0, 0], 
    [5, 2, 0, 0, 0, 0, 0, 0, 0], 
    [0, 8, 7, 0, 0, 0, 0, 3, 1], 
    [0, 0, 3, 0, 1, 0, 0, 8, 0], 
    [9, 0, 0, 8, 6, 3, 0, 0, 5], 
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 7, 4], 
    [0, 0, 5, 2, 0, 6, 3, 0, 0]],np.int)
board=np.array([#medium 1min 49e
    [5, 3, 0, 0, 7, 0, 0, 0, 0], 
    [6, 0, 0, 1, 9, 5, 0, 0, 0], 
    [0, 9, 8, 0, 0, 0, 0, 6, 0], 
    [8, 0, 0, 0, 6, 0, 0, 0, 3], 
    [4, 0, 0, 8, 0, 3, 0, 0, 1], 
    [7, 0, 0, 0, 2, 0, 0, 0, 6], 
    [0, 6, 0, 0, 0, 0, 2, 8, 0], 
    [0, 0, 0, 4, 1, 9, 0, 0, 5], 
    [0, 0, 0, 0, 8, 0, 0, 7, 9]],np.int)
# board=np.array([#semi-hard 10m 56e
#     [5, 3, 0, 0, 7, 0, 0, 0, 0], 
#     [0, 0, 0, 1, 9, 5, 0, 0, 0], 
#     [0, 9, 8, 0, 0, 0, 0, 6, 0], 
#     [8, 0, 0, 0, 6, 0, 0, 0, 0], 
#     [4, 0, 0, 8, 0, 0, 0, 0, 1], 
#     [7, 0, 0, 0, 0, 0, 0, 0, 6], 
#     [0, 6, 0, 0, 0, 0, 2, 8, 0], 
#     [0, 0, 0, 4, 1, 9, 0, 0, 5], 
#     [0, 0, 0, 0, 8, 0, 0, 7, 0]],np.int)
# board=np.array([#hard 65e ??? 
#     [0, 0, 0, 0, 0, 0, 1, 0, 8], 
#     [0, 0, 0, 0, 0, 0, 3, 0, 0], 
#     [7, 0, 0, 0, 0, 9, 0, 0, 0], 
#     [0, 0, 0, 6, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 3, 1, 0, 0, 0, 0], 
#     [5, 0, 0, 0, 0, 0, 0, 2, 0], 
#     [0, 0, 8, 5, 0, 0, 0, 4, 0], 
#     [0, 1, 3, 0, 0, 0, 0, 0, 0], 
#     [0, 6, 0, 0, 0, 2, 0, 0, 0]],np.int)


possible={}

def detect_row(row):
    return set(board[row,:][board[row,:]!=0])

def detect_col(col):
    return set(board[:,col][board[:,col]!=0])

def detect_sqr(x,y):
    l=board[(x//3)*3:(x//3)*3+3,(y//3)*3:(y//3)*3+3]
    return set(l[l!=0])

def detect_possible():
    ...

def is_valid_all(_board):
    for i in range(9):
        l=_board[:,i]
        if Counter(l[l!=0]).most_common()[0][1]!=1:
            return False
    for i in range(9):
        l=_board[i,:]
        if Counter(l[l!=0]).most_common()[0][1]!=1:
            return False
    for (x,y) in [
        (1,1),(4,1),(7,1),
        (1,4),(4,4),(7,4),
        (1,7),(4,7),(7,7)]:
        l=detect_sqr(x,y)
        if Counter( l ).most_common()[0][1] !=1 :
            return False
    return True

def detect_cells():
    x,y=board.shape
    for i in range(x):
        for j in range(y):
            if board[i,j]==0:
                p_row=detect_row(i  )
                p_col=detect_col(j  )
                p_sqr=detect_sqr(i,j)
                possible[(i,j)]=list(set([1,2,3,4,5,6,7,8,9]) - (p_row | p_col | p_sqr))
                
                if len(possible[(i,j)])==1:
                    board[i,j]=possible[(i,j)][0]
                    del possible[(i,j)]


def back_track(board_,keys_,ans_):

    if not is_valid_all(board_):
        return False
    if len(keys_)==0:
        print(board_)
        return ans_
    (x,y)=keys_.pop(0)
    for ans in possible[(x,y)]:
        board_[x,y]=ans
        if back_track(np.array(board_),list(keys_),ans_+f" ({x},{y}):[{ans}]"):
            return True

detect_cells()
# print([len(i) for i in possible.values()])
back_track(board,list(possible.keys()),"")