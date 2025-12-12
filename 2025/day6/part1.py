import os
import operator

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")

OPERATORS = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y, 
    "/": lambda x, y: x/y
}

with open(FILENAME, "r") as f:
    data = f.read()
    lines = data.split("\n")
    operations = lines[-1].split()

split_lines = [list(map(int, line.split())) for line in lines[:-1]] # Convert to a list of integers, to avoid int() later on.


total = 0
for op, nums in zip(operations, zip(*split_lines)):
    res = nums[0]
    for num in nums[1:]:
        res = OPERATORS[op](res, num)
    
    total += res
    
print(total)
        