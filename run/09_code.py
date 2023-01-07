
import numpy as np

_xhat = np.array([1,0])
_yhat = np.array([0,1])

def follow_head( head_loc:np.ndarray, tail_loc:np.ndarray, head_move_dir:str ):
    move_directions = {'U':_yhat, 'R':_xhat, 'D':-_yhat, 'L':-_xhat}
    # print(head_loc)
    # print(tail_loc)
    head_loc = head_loc + move_directions[head_move_dir]
    # print(head_loc)
    loc_diff = head_loc - tail_loc
    if np.sum(np.abs(loc_diff)) == 3:
        # diagonal rule
        tail_loc  = tail_loc + (np.sign(loc_diff) * (_xhat + _yhat))
    else:
        tail_loc  = tail_loc + ( (np.abs(loc_diff) > 1)  * np.sign(loc_diff) * (_xhat + _yhat) )

    # print(loc_diff)
    # print(tail_loc)
    # print('--')
    return head_loc, tail_loc

def perform_move_sequence( head_moves:list, head_start = np.array([0, 0]), tail_start = np.array([0, 0]) ):
    # maparr = np.zeros([7,7])
    head_loc = head_start
    tail_loc = tail_start
    # maparr[head_loc[0], head_loc[1]] = 9
    # maparr[tail_loc[0], tail_loc[1]] = 1
    # print(maparr.transpose()[-1::-1])
    tail_positions = set()
    tail_positions.add(tuple(tail_loc)) # need tuple for set
    for move in head_moves:
        for i in range(move[1]):
            head_loc, tail_loc = follow_head( head_loc, tail_loc, move[0] )
            tail_positions.add(tuple(tail_loc)) # different positions of tail
            # maparr[head_loc[0], head_loc[1]] = 9
            # maparr[tail_loc[0], tail_loc[1]] = 1
            # print(maparr.transpose()[-1::-1])
    # print(maparr.sum())
    return tail_positions

if __name__ == "__main__":
    filename = "E:/Dropbox/py_projects/adventofcode/inputs/09_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/09.1_input.txt"
    with open(filename) as file:
        filestr = file.read( ).split('\n')
        headmoves = [line.split() for line in filestr]
        for move in headmoves:
            move[1] = int(move[1])
    # print(headmoves)

    tail_pos = perform_move_sequence( headmoves )

    print(tail_pos)
    print(len(tail_pos))
        
        