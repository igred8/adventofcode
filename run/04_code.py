import csv

input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/04_input.txt"
# input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/04.1_input.txt"

interval_list = []

with open(input_file_name) as file:
    csv_reader = csv.reader(file, delimiter='\n')
    for row in csv_reader:
        if row == []:
            row = ['\n']
        row = row[0].split(',')
        interval1 = [int(n) for n in row[0].split('-')]
        interval2 = [int(n) for n in row[1].split('-')]
        interval_list.append( [interval1, interval2] )

def interval_inside(interval1, interval2):
    inside = False
    if (interval1[0]>=interval2[0]) and (interval1[1]<=interval2[1]):
        inside = True
    return inside

interval_counter = 0
for i in interval_list:
    # print(i)
    # overlap = [max([i[0][0], i[1][0]]), min([i[0][1],i[1][1]])]
    # print(overlap)
    inside12 = interval_inside(i[0], i[1])
    inside21 = interval_inside(i[1], i[0])
    if inside12 or inside21:
        interval_counter += 1
        # print('one contains the other')
# print(len(interval_list))
# print(interval_counter)


interval_counter = 0
for i in interval_list:
    # print(i)
    overlap = [max([i[0][0], i[1][0]]), min([i[0][1],i[1][1]])]
    # print(overlap)
    if overlap[0]<=overlap[1]:
        interval_counter += 1
    # elif overlap[0]==overlap[1]:


print(interval_counter)
