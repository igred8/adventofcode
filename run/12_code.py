import numpy as np

alt_start = 0
alt_end = 25
up = np.array([-1,0])
right = np.array([0,1])
down = np.array([1,0])
left = np.array([0,-1])

class PathFinder():

    def __init__(self, charmap:np.ndarray, altmap:np.ndarray) -> None:
        self.charmap = charmap
        self.altmap = altmap
        self.visitmap = (charmap == 'S')
        self.travelmap = np.zeros_like(altmap)
        self.start = np.argwhere( self.visitmap )[0]
        self.end = np.argwhere( charmap == 'E' )[0]

        self.altmap[charmap =='S'] = alt_start
        self.altmap[charmap =='E'] = alt_end

    def check_position( self, alt_current, alt_temp, visited):
               
        if not visited:
            if alt_temp in [alt_current-1, alt_current, alt_current+1]:
                return True
            return False
        return False

    def move(self, pos_current:np.ndarray):
        pos_new = pos_current.copy()
        moves = [up, right, down, left]

        for move in moves:
            pos_temp = pos_current + move
            # print(f'moved to: {pos_temp}')
            
            if (pos_temp[0]>=0) and (pos_temp[1]>=0):
                try:
                    alt_current = self.altmap[pos_current[0],pos_current[1]]
                    print(f'current: pos={pos_current}, altitude={alt_current}')
                    alt_temp = self.altmap[pos_temp[0],pos_temp[1]]
                    visit_temp = self.visitmap[pos_temp[0],pos_temp[1]]
                    print(f'check: pos={pos_temp}, altitude={alt_temp}')
                    print(f'visited? {visit_temp}')
                    temp_pos_ok = self.check_position( alt_current, alt_temp, visit_temp )
                    
                    if temp_pos_ok:
                        pos_new = pos_temp.copy()
                        break
                except IndexError:
                    # catch going outside of map array
                    continue
            else:
                # catch negative indexing. it is allowed in lists and ndarrays, so must exclude
                continue
        
        return pos_new, temp_pos_ok

    def pathfind(self):
        pos_current = self.start.copy()
        path = [pos_current]
        i = 0
        while (not np.all(pos_current == self.end)) and (i<10000) :
            pos_temp, temp_ok = self.move( pos_current )
            if temp_ok:
                pos_current = pos_temp.copy()
                path.append( pos_current )
                self.visitmap[pos_current[0], pos_current[1]] = True
                self.travelmap[pos_current[0], pos_current[1]] = len(path)
            else:
                # go back one step in path                
                pos_current = path.pop()

            i += 1
        return len(path)



if __name__ == "__main__":

    filename = "E:/Dropbox/py_projects/adventofcode/inputs/12_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/12.1_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/12.2_input.txt"
    
    with open(filename) as file:
        lines = file.read()
        charmap = [[c for c in line] for line in lines.split("\n")]
        charmap = np.array(charmap)
        
        altmap = [[ord(c)-97 for c in line] for line in lines.split("\n")]
        altmap = np.array(altmap)
    
    # for line in lines:
    #     print(line)
    # print(charmap)
    # print(altmap)
    # print(np.argwhere(altmap == -14) )

    pf = PathFinder(charmap, altmap)
    print(pf.altmap)
    # print(pf.start[0])
    # print(pf.altmap[0,1])
    # pos_new = pf.move(pf.start)
    # print(pos_new)
    try:
        nsteps = pf.pathfind()
        print(nsteps)
        print(pf.visitmap)
    except IndexError as err:
        print(err)
        

    # pf.altmap = pf.altmap - 26
    # pf.altmap[pf.visitmap] = 0
    np.savetxt("E:/Dropbox/py_projects/adventofcode/inputs/12_output.txt", pf.travelmap, fmt='%d', delimiter=' ')
    np.savetxt("E:/Dropbox/py_projects/adventofcode/inputs/12_output-alt.txt", pf.altmap, fmt='%d', delimiter=' ')