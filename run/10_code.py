
def read_signal( operations:list ):

    signal = [1]
    for op in operations:
        if op[0] == 'noop':
            signal.append( signal[-1] )
        elif op[0] == 'addx':
            signal.append( signal[-1] )
            signal.append( signal[-1] + int(op[1]) )
    return signal

def calc_signal_strength( signal:list, start:int, period:int):
    signal_strength = 0
    for i in range(start-1, len(signal), period):
        signal_strength += (i+1) * signal[i]
    return signal_strength

def draw_sprite( signal:list ):
    screen_width = 40
    screen_height = 6
    screen2d = []
    for j in range(screen_height):
        start = j*screen_width
        end = start + screen_width
        rowstr = ''
        for i,s in enumerate(signal[start:end]):
            if i in [s-1, s, s+1]:
                c = '#'
            else:
                c = '.'
            rowstr += c
        screen2d.append( rowstr ) 
    return screen2d

if __name__ == '__main__':
    filename = "E:/Dropbox/py_projects/adventofcode/inputs/10_input.txt"
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/10.1_input.txt"
    with open(filename) as file:
        filestr = file.read()
        lines = filestr.split('\n')
        operations = [ l.split() for l in lines ]
    signal = read_signal( operations )
    signal_strength = calc_signal_strength( signal, 20, 40 )
    print(signal_strength)

    screen2d = draw_sprite( signal )
    for row in screen2d:
        print(row)