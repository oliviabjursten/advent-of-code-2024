import re

# -----------------PART 1-----------------
path = '/Users/-/adventofcode2024/input_day3.txt'

with open(path, 'r', encoding='utf-8') as file:
    fileCont = file.read()

pattern = r"mul\((\d+),(\d+)\)" 
matches = re.findall(pattern, fileCont)
total_sum = sum(int(x) * int(y) for x, y in matches)

#print(matches)
#print(total_sum)

# -----------------PART 2-----------------

calculation_enabled = True
total_sum2 = 0


segments = re.split(r"(do\(\)|(don't))", fileCont)

for segment in segments:

    if not segment:
        continue
    
    if "do()" in segment:
        calculation_enabled = True
        continue
    
    if "don't" in segment:
        calculation_enabled = False
        continue

    if calculation_enabled:
        matches = re.findall(pattern, segment)
        for x, y in matches:
            product = int(x) * int(y)
            total_sum2 += product

print(total_sum2)
#------
