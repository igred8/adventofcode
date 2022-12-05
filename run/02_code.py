import csv
from enum import IntEnum


input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/02_input.txt"
# input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/02.1_input.txt"
games_list = []
with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    for row in csv_reader:
        if row == []:
            row = ['\n']
        games_list.append( row[0].split(" ") )

# print(games_list[:20])
rps_convert = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}
class RPSAction(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

games_list_actions = [ [RPSAction(rps_convert[row[0]]), RPSAction(rps_convert[row[1]])] for row in games_list ]

score_loss = 0
score_tie = 3
score_win = 6

def rps_play( action_elf, action_you ):
    


    score = 0
    if action_elf == action_you:
        score = action_you.value + 1 + score_tie
        # print('tie')
    elif (action_elf.value + 1)%3 == action_you:
        score = action_you.value + 1 + score_win
        # print('action_you wins')
    else:
        score = action_you.value + 1 + score_loss
        # print('action_elf wins')
    
    return score

score_total = 0
for i in range(len(games_list_actions)):
    
    # print(*games_list_actions[i])
    
    score_i = rps_play( *games_list_actions[i])
    # print(f'score = {score_i}')
    score_total += score_i

print(score_total)

rps_convert = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':3, 'Z':6}
games_list_action_outcome = [ [ RPSAction(rps_convert[row[0]]), rps_convert[row[1]] ] for row in games_list ]


def rps_decode( action_elf, outcome):
    score = 0
    if outcome == score_tie:
        score = action_elf.value + 1 + score_tie
    elif outcome == score_win:
        score = (action_elf.value + 1)%3 +1 + score_win
    elif outcome == score_loss:
        score = (action_elf.value - 1)%3 +1 + score_loss
    else:
        print("not a valid outcome")
    
    return score

score_decoded_total = 0
for i in range(len(games_list_action_outcome)):
    # print(games_list_action_outcome[i])
    score_i = rps_decode( *games_list_action_outcome[i])
    # print(score_i)
    score_decoded_total += score_i

print(score_decoded_total)