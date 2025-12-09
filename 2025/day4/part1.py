import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
NUMCOUNT = 12

with open(FILENAME, "r") as f:
    grid = []
    grid = [row for row in f.read().split("\n")]
    # line = f.readline()
    # while line != "":
    #     grid.append([col for col in line])
    #     line = f.readline()

cols = len(grid[0])       # How many cols in a row
rows = len(grid)          # How many rows there are

total = 0

for i in range(rows):   # Rows
    for j in range(cols):  # Colums
        if grid[i][j] != "@":   # If grid is not @ then we can skip this gridsquare
            continue
        if (i==0 and j==0) or (i==rows-1 and j==0) or (i==0 and j==cols-1) or (i==rows-1 and j==cols-1):
            # We are at a corner - cannot have >= 4 adjacent @ symbols because only 3 adjacent grid squares so always valid.
            total += 1
            continue
        
        count = 0
        
        if i != 0:  # Check (up to) 3 above as we are not checking the top row
            if grid[i-1][j] == "@":     # N square
                count += 1
            if (j != 0) and (grid[i-1][j-1]) == "@": # NW square
                count += 1 
            if (j != cols-1) and grid[i-1][j+1] == "@":   # NE square
                count += 1
        if i != rows-1: # Check (up to) 3 below as we are not checking the top row
            if grid[i+1][j] == "@":     # S square
                count += 1
            if (j != 0) and (grid[i+1][j-1]) == "@": # SW square
                count += 1 
            if (j != cols-1) and grid[i+1][j+1] == "@":   # SE square
                count += 1
        if j != 0:
            if grid[i][j-1] == "@": # W square
                count += 1
        if j != cols-1:
            if grid[i][j+1] == "@": # E square
                count += 1
        if count < 4:
            total += 1
        
    
print(total)
             