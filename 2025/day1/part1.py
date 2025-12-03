# Password is how many times dial shows zero during turn combinations.
# Dial is circular
# INPUT FORMAT: file, each line:
#                               LNUM || RNUM
# If LNUM -> "rotate" dial left NUM times. If RNUM -> "rotate dial right NUM times"

# NOTES
# Iterate through file, Sum NUMs together, if L then add negative NUM.
# After every "turn" instruction -> if total % 100 = 0 then count ++
# Count is password.

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
            num = -num
    
        total += num
        if total % DIAL_SIZE == 0:
            count += 1

pwd = count
print(pwd)