import csv

# input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/03_input.txt"
input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/03.1_input.txt"
items_list = []

with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    for row in csv_reader:
        if row == []:
            row = ['\n']
        row = row[0]
        items_list.append( [row[:len(row)//2], row[len(row)//2:]] )

def letter_to_priority( char ):
    priority = 0 
    if (ord(char)>=65) and (ord(char)<=90):
        priority = ord(char) - 65 + 26 + 1
    elif (ord(char)>=97) and (ord(char)<=122):
        priority = ord(char) - 97 + 1
    return priority

priority_total = 0
for rucksack in items_list:
    print(rucksack)

    pack1 = list( set(rucksack[0]) ) # list to iterate over, set to remove duplicates
    pack2 = set( rucksack[1] ) # set to check in
    common_items = []
    for i in pack1:
        if i in pack2:
            common_items.append(i)
    print(common_items)
    for char in common_items:
        priority_char = letter_to_priority( char )
        print(priority_char)
        priority_total += priority_char

print(f"sum of priority of common items = {priority_total}")

