import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")


with open(FILENAME, "r") as f:
    ranges = [x for x in f.read().split(",")]

_sum = 0

for r in ranges:
    start, end = r.split("-")
    for num in range(int(start), int(end) + 1):
        length = len(str(num))
        if length % 2 == 1:
            # Num is odd length
            continue
        first_half = str(num)[:length // 2]
        second_half = str(num)[length // 2:]
        if first_half == second_half:
            _sum += num

print(_sum)