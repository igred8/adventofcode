### Can't get the right answer on this one :(  

import csv

class Dir():
    def __init__(self, name) -> None:
        self.name = name
        self.size = 0
        self.parent = None
        self.contains = dict()
        self.explored = False

class File():
    def __init__(self, name) -> None:
        self.name = name
        self.size = 0

class DirStructure():
    def __init__(self) -> None:
        self.structure = None

    def make_dir_structure( self, lines, verbose=False ):

        current_dir = Dir('/_dir')
        self.structure = {current_dir.name:current_dir}

        for i,l in enumerate(lines):
            # print(f"/ size = {dir_set['/'].size}")
            try:
                if verbose:
                    print(f'current dir, {current_dir.name} contains:')
                    [print(o) for o in current_dir.contains]
                    print(f'current dir parent = {current_dir.parent.name}')
                    print('---')
            except:
                pass

            if verbose: print(f"line {i:d} = {l}")

            if '$ cd /' == l:
                current_dir = self.structure['/_dir']
                continue
            if '$ cd ..' == l:
                current_dir = current_dir.parent
                continue
            if '$ cd ' in l:
                current_dir = current_dir.contains[l[5:]+'_dir']
                
                
                # # print(l[5:])
                # current_dir_l = Dir(l[5:])
                # current_dir_l.parent = current_dir
                # if current_dir_l.name not in dir_set:
                #     current_dir = current_dir_l
                #     # print('adding to set')
                #     dir_set[ current_dir.name ] = current_dir
                # else:
                #     current_dir = dir_set[current_dir_l.name]
                # # print(f'cur dir = {current_dir.name}')
                # # print(f'parent = {current_dir.parent.name}')
                continue
            
            if '$ ls' in l:
                continue

            lprops = l.split()
            if lprops[0] == 'dir':
                dirname_ = lprops[1] + '_dir'
                if dirname_ not in current_dir.contains:
                    newdir = Dir(dirname_)
                    newdir.parent = current_dir
                    current_dir.contains[dirname_] = newdir 
                continue

            
            file_name = lprops[1] + '_file'
            if file_name not in current_dir.contains:
                f = File(file_name)
                try:
                    f.size = int( lprops[0] )
                except ValueError:
                    print(f'ERROR!\nCannot convert {lprops[0]} to int')
                    print(f'current dir = {current_dir.name}, file name = {f.name}')
                current_dir.contains[file_name] = f
                current_dir.size += f.size # update size of directory
                continue

        # self.structure = dir_set

        # return dir_set
    
    def calc_dir_sizes(self, verbose=False):

        # DFS
        # make LIFO queue
        # pop until empty
        # start from root
        node_list = [self.structure['/_dir']]
        while node_list:
            
            if verbose:
                print('node_list:')
                for n in node_list:
                    print(n.name)

            node = node_list.pop()
            if verbose: print(f'at node: {node.name}, init_size = {node.size:d}')
            
            # if node.explored:
            #     continue
            # node.explored = True

            # propagate size back to parents
            node_back = node
            while node_back.parent:
                if verbose: print(f'node parent = {node_back.parent.name}')
                node_back.parent.size += node.size
                node_back = node_back.parent
            
            # add to queue if obj is a directory
            for objname, obj in node.contains.items():
                if type(obj) is Dir:
                    node_list.append( obj )

        return 0

    def flag_small_directories( self, max_size = 100_000, verbose=False):
        
        small_dirs = {}

        # DFS
        # make LIFO queue
        # pop until empty
        # start from root
        node_list = [self.structure['/_dir']]

        while node_list:
            
            if verbose:
                print('node_list:')
                for n in node_list:
                    print(n.name)

            node = node_list.pop()
            if verbose: print(f'at node: {node.name}')
            
            if node.size <= max_size:
                small_dirs[node.name] = node

            # add to queue if obj is a directory
            for objname, obj in node.contains.items():
                if type(obj) is Dir:
                    node_list.append( obj )

        return small_dirs




if __name__ == '__main__':
    
    input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/07_input.txt"
    # input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/07.1_input.txt"
    # input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/07.2_input.txt"

    lines = []

    total_size_max = 100_000

    with open(input_file_name) as file:
        csv_reader = csv.reader(file, delimiter='\n')
        for row in csv_reader:
            # print(row)
            if row == []:
                row = [' ']
            
            # row = row[0].split()
            lines.append( row[0] )

    fs = DirStructure()
    fs.make_dir_structure(lines, verbose=False)
    
    fs.calc_dir_sizes(verbose=True)

    small_dirs = fs.flag_small_directories(max_size=total_size_max)

    sum_of_small_dir_sizes = 0
    for n,d in small_dirs.items():
        print(f"{n:12} : {d.size:d}")
        sum_of_small_dir_sizes += d.size
    

    print(f"Sum of small directory sizes = {sum_of_small_dir_sizes:d}")
    if sum_of_small_dir_sizes == 1895667:
        print('same wrong answer :[')
    else:
        print('new answer')
