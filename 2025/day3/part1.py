import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")


with open(FILENAME, "r") as f:
    banks = [x for x in f.read().split("\n")]

total = 0

for bank in banks:
    highest_num = max(bank[:-1])            # [:-1] as 2 digit always > last digit.
    index = bank[:-1].index(highest_num)    # return first index that num is found in
    second_num = max(bank[index+1:])        # Iterate over rest of list and find second highest.
    res = int(highest_num + second_num)     # Should work, concatenate e.g. "50" to int

    total += res

print(total)
