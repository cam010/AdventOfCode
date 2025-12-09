import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
NUMCOUNT = 12

with open(FILENAME, "r") as f:
    banks = [x for x in f.read().split("\n")]

total = 0
for bank in banks:
    float = len(bank) - NUMCOUNT + 1
    i = 0
    
    num = ""
    
    for _ in range(NUMCOUNT):
        bank = bank[i:]
        next_num = max(bank[:float])
        index = bank.index(next_num) 
        i = index + 1
        float -= index
        
        num += next_num
    total += int(num)

print(total)