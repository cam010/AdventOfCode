import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")

with open(FILENAME, "r") as f:
    data = f.read().split("\n")
    split_point = data.index("")
    
    ranges = data[:split_point]
    ids = data[split_point+1:]

total = 0
for _id in ids:
    for _range in ranges:
        start, end = _range.split("-")
        if int(_id) >= int(start) and int(_id) <= int(end):
            total += 1
            break

print(total)