
input_file_name = "E:/Dropbox/py_projects/adventofcode/inputs/06_input.txt"
stream = ''
with open(input_file_name) as file:
    stream += file.read() 

# stream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # 7, 19
# stream = 'bvwbjplbgvbhsrlpgdmjqwftvncz' # 5, 23
# stream = 'nppdvjthqldpwncqszvftbrmjlhg' # 6, 23
# stream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 10, 29
# stream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 11, 26

print(stream)

marker = ''
for i,char in enumerate(stream):
    print(marker)
    if len(marker) == 14:
        break
    
    if char in marker:
        char_index = marker.index(char)
        marker = marker[char_index+1:]
        marker += char
        continue
    marker += char
    
print(i)