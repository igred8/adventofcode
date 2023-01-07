
import numpy as np

_xhat = np.array([1,0])
_yhat = np.array([0,1])
_move_directions = {'U':_yhat, 'R':_xhat, 'D':-_yhat, 'L':-_xhat}

class Rope():
    
    def __init__(self, rope_len) -> None:
        self.len = rope_len
        self.body = np.zeros(shape=[rope_len, 2], dtype=int)
    
    def _move_head( self, head_move_dir ):
        self.body[0] = self.body[0] + _move_directions[head_move_dir]
        
    def _follow(self, ahead_loc, behind_loc ):
        ''' assumes one step move was made so that ahead and behind are at most 2+1=3 manhattan distance away '''
        loc_diff = ahead_loc - behind_loc
        if np.sum(np.abs(loc_diff)) == 3:
            # diagonal rule
            behind_loc  = behind_loc + (np.sign(loc_diff) * (_xhat + _yhat))
        else:
            behind_loc  = behind_loc + ( (np.abs(loc_diff) > 1)  * np.sign(loc_diff) * (_xhat + _yhat) )

        return ahead_loc.astype(int), behind_loc.astype(int)
    
    def _move_body( self ):

        for i in range(1, self.len):
            
            _, self.body[i] = self._follow( self.body[i-1], self.body[i] )


    def perform_move_sequence( self, head_moves:list ):
        
        tail_positions = set()
            
        for move in head_moves:
            for _ in range(move[1]):
                self._move_head( move[0] )
                self._move_body()
                tail_positions.add( tuple( self.body[-1] ) ) # tuples for set (hashable)


        return tail_positions

if __name__ == "__main__":
    filename = "E:/Dropbox/py_projects/adventofcode/inputs/09_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/09.1_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/09.2_input.txt"

    with open(filename) as file:
        filestr = file.read( ).split('\n')
        headmoves = [line.split() for line in filestr]
        for move in headmoves:
            move[1] = int(move[1])
    # print(headmoves)

    rope = Rope(rope_len=10)
    tail_positions = rope.perform_move_sequence( headmoves )
    # for tp in tail_positions:
    #     print(tp)
    print(len(tail_positions))
        