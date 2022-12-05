import csv

input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/03_input.txt"
# input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/03.1_input.txt"
items_list = []
items_list_unsplit = []

with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    for row in csv_reader:
        if row == []:
            row = ['\n']
        row = row[0]
        items_list.append( [row[:len(row)//2], row[len(row)//2:]] )
        items_list_unsplit.append(row)

def letter_to_priority( char ):
    priority = 0 
    if (ord(char)>=65) and (ord(char)<=90):
        priority = ord(char) - 65 + 26 + 1
    elif (ord(char)>=97) and (ord(char)<=122):
        priority = ord(char) - 97 + 1
    return priority

priority_total = 0
for rucksack in items_list:
    # print(rucksack)

    pack1 = list( set(rucksack[0]) ) # list to iterate over, set to remove duplicates
    pack2 = set( rucksack[1] ) # set to check in
    common_items = []
    for i in pack1:
        if i in pack2:
            common_items.append(i)
    # print(common_items)
    for char in common_items:
        priority_char = letter_to_priority( char )
        # print(priority_char)
        priority_total += priority_char

print(f"sum of priority of common items = {priority_total}")


def group_common_prriority( group ):
    common = set(group[0])
    for pack in group[1:]:
        # print(common)
        common = common.intersection(pack)
    
    common_priority = 0
    for char in common:
        common_priority +=  letter_to_priority(char)
    return common_priority

GROUP_SIZE = 3
common_item_group_priority = 0
group_temp = []
for i,pack in enumerate(items_list_unsplit):
    if len(group_temp) < GROUP_SIZE:
        group_temp.append(pack)
        # print(group_temp)
        if len(group_temp) == GROUP_SIZE:
            common_item_group_priority += group_common_prriority(group_temp)

        # print(common_item_group_priority)
    else:
        group_temp = [pack]

print(f"sum of priorities of badges {common_item_group_priority}")