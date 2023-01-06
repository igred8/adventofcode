import numpy as np

def count_visible_trees( treemap ):
    nrows, ncols = treemap.shape
    visible_count = 2*(nrows+ncols)-4
    for i in range(1, nrows-1):
        for j in range(1, ncols-1):
            temp = treemap[:i,j]
            if treemap[i,j] > temp.max():
                visible_count += 1
                # print(temp)
                # print('--')
                continue
            
            temp = treemap[i+1:, j]
            if treemap[i,j] > temp.max():
                visible_count += 1
                # print(temp)
                # print('--')
                continue
            
            temp = treemap[i, :j]
            if treemap[i,j] > temp.max():
                visible_count += 1
                # print(temp)
                # print('--')
                continue
            
            temp = treemap[i, j+1:]
            if treemap[i,j] > temp.max():
                visible_count += 1
                # print(temp)
                # print('--')
                continue
    return visible_count

def most_scenic_tree( treemap ):
    nrows, ncols = treemap.shape

    scenic_scores = np.zeros_like(treemap)

    for i in range(nrows):
        for j in range(ncols):
    
            hij = treemap[i,j]
            print(f"i={i:d}, j={j:d}, hij={hij:d}")
            scenes = [0,0,0,0]
            for d, (direction,(istep, jstep)) in enumerate({'up':[-1,0],'right':[0,1],'down':[1,0],'left':[0,-1]}.items()):
                print(direction)
                # print(f'istep = {istep:d}')
                # print(f'jstep = {jstep:d}')
                ii = i + istep
                jj = j + jstep
                
                if (ii not in range(nrows)) or (jj not in range(ncols)): 
                    # tree is on edge and has 0 scenic score
                    scenic_scores[i,j] = 0
                    break
                temp = treemap[ ii, jj ]
                
                while True:
                    print(temp)
                    
                    scenes[d] = scenes[d] + 1
                    if hij <= temp: 
                        break
                    
                    ii += istep
                    jj += jstep
                    if (ii not in range(nrows)) or (jj not in range(ncols)): 
                        # tree is on edge 
                        break
                    temp = treemap[ii, jj]
            print(scenes)
            ss = 1
            for s in scenes:
                ss *= s
            scenic_scores[i,j] = ss
    print(scenic_scores)

    print(scenic_scores.max())

            

    



if __name__ == '__main__':
    
    input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/08_input.txt"
    # input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/08.1_input.txt"
    


    with open(input_file_name) as file:
        
        filestr = file.read()
        filestr = filestr.split('\n')
        treemap = np.array( [[int(c) for c in line] for line in filestr] , dtype=int)
        
    print(type(treemap))
    print(treemap)

    # visible_trees = count_visible_trees(treemap)
    # print(f'number of visible trees = {visible_trees:d}')

    most_scenic_tree( treemap )