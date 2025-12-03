# NOTES
# Full turns = NUM DIV 100
# Then, calculate if 1 more turn by total +- NUM MOD 100. If total <= 0 or total >= 100 then 1 more turn (if prev total wasn't already 0, 100). New total = total MOD 100

# ANSWER CORRECT

import os

DIAL_SIZE = 100
FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")

total = 50
count = 0

with open(FILENAME, "r") as f:
    while True:
        line = f.readline()
        
        if line == "":
            # End of File
            break
    
        # No need for input verification
        num = int(line[1:])  # first character is L/R
        if line.startswith("L"):
            neg = True
        else:
            neg = False

        prev_total = total
        
        diff = num // 100
        total = total - (num % 100) if neg else total + (num % 100) # Have to mod positive because negative works different (-43 % 100 = 57 not 43)
        
        if (total <= 0 and prev_total != 0) or (total >= 100 and prev_total != 100):
            # Only have to add 1 as max change in total is +- 99 which is 0 or 1 turns through zero. 
            diff += 1
            
        total = total % 100
        
        count += diff

pwd = count
print(pwd)