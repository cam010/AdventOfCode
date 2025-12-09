import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")

with open(FILENAME, "r") as f:
    data = f.read().split("\n")
    split_point = data.index("")
    
    ranges = data[:split_point]

_pass = True
while _pass:
    _pass = False
    for i1, n1 in enumerate(ranges):
        new_ranges = []
        merged = False
        start1, stop1 = n1.split("-") 
        for i2, n2 in enumerate(ranges):
            if i1 == i2:
                continue
            if merged:
                # Range has merged, add all remaining ranges to new list and start new pass
                new_ranges.append(n2)
                continue
                
            start2, stop2 = n2.split("-")
            if int(start1) <= int(stop2) and int(start2) <= int(stop1): 
                # ranges overlap
                # Combine ranges
                start = min(int(start1), int(start2))
                end = max(int(stop1), int(stop2))

                # Add new range to new list
                new_range = str(start) + "-" + str(end)
                new_ranges.append(new_range)
                merged = True
                _pass = True
            else:
                # Ranges don't overlap
                new_ranges.append(n2)
                
        if not merged:
            # If not merged, skip to next i1 n1
            continue
        
        if merged:
            # Merged, skip to next pass
            ranges = [x for x in new_ranges]
            break
            

ids = 0
for _range in ranges:
    start, stop = _range.split("-")
    count = int(stop) - int(start) + 1  # +1 to include the startpoint i.e. 10-14 should be 5.
    ids += count


print(ids)