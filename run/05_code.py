import csv

input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/05_input.txt"
# input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/05.1_input.txt"

lines = []

with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    rn = 0
    rownew = []
    for row in csv_reader:
        # print(row)
        if row == []:
            row = [' ']
            rownew.append(rn)
        else:
            rn += 1
        
        # row = row[0].split()
        lines.append( row )
# print(rownew)
# print(lines[rownew[0]-1])

nstacks = len(lines[rownew[0]-1][0].split())
print(f'number of stacks = {nstacks:d}')
stacks = [ [] for _ in range(nstacks)]

# make LIFO stacks (lists)
charindex = range(1,nstacks*3 + nstacks-1,4)
for l in lines[rownew[0]-2::-1]:
    for i,c in enumerate(charindex):
        if l[0][c] != ' ':
            stacks[i].append(l[0][c])
for s in stacks:
    print(s)

# make list of instructions
instructions = []
for l in lines[rownew[0]+1:]:
    lele = l[0].split()
    instructions.append([int(lele[1]), int(lele[3]), int(lele[5])])
# print(instructions)

# def move_blocks( nblocks, stack_from, stack_to):
#     i = 0
#     while (i<nblocks) and (stack_from != []):
#         block = stack_from.pop()
#         stack_to.append(block)
#         i += 1
#     return stack_from, stack_to

# for instr in instructions:
#     nblocks, ifrom, ito = instr[0], instr[1]-1, instr[2]-1
#     stack_from = stacks[ifrom]
#     stack_to = stacks[ito]

#     stack_from, stack_to = move_blocks( nblocks, stack_from, stack_to)
#     stacks[ifrom] = stack_from
#     stacks[ito] = stack_to

# message = ''
# for s in stacks:
#     message += s.pop()
# print(message)


def move_blocks_as_one( nblocks, stack_from, stack_to):
    for b in stack_from[-nblocks:]:
        stack_to.append(b)
    stack_from = stack_from[:-nblocks]
    return stack_from, stack_to

print('---')
# print(stacks)

for instr in instructions:
    nblocks, ifrom, ito = instr[0], instr[1]-1, instr[2]-1
    stack_from = stacks[ifrom]
    stack_to = stacks[ito]

    stack_from, stack_to = move_blocks_as_one( nblocks, stack_from, stack_to)
    stacks[ifrom] = stack_from
    stacks[ito] = stack_to

    # print(stacks)

message = ''
for s in stacks:
    print(s)
    if s != []:
        message += s.pop()
print(message)