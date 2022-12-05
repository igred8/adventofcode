import csv

input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/01_input.txt"
calories_list = []
with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    for row in csv_reader:
        if row == []:
            row = ['\n']
        calories_list += row

# print(calories_list)
# print(type(calories_list[0]))

elf_number = 0
elf_calories_list = []

elf_calories_current = 0
for cals in calories_list:
    try:
        cals = int(cals)
        elf_calories_current += cals
    
    except ValueError:
               
        elf_number += 1
        elf_calories_list.append(elf_calories_current)
        elf_calories_current = 0

elf_calories_list.sort(reverse=True)
print(elf_calories_list[:3])
print(f'top 3 elves carry {sum(elf_calories_list[:3]):d} calories')
