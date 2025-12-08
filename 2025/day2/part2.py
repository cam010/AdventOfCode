import os

FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")


with open(FILENAME, "r") as f:
    ranges = [x for x in f.read().split(",")]

_sum = 0

for r in ranges:
    start, end = r.split("-")
    for num in range(int(start), int(end) + 1):
        length = len(str(num))

        invalid = False
        i = 1
        while i <= length / 2:
            # When i > length / 2 -> cant have 2+ sections that are the same
            if length % i == 0:
                # if length % i != 0 then cant have integer number of i length sections
                j = i
                section1 = str(num)[0:j]
                could_be_valid = False
                while j <= length and not could_be_valid:
                    section = str(num)[j: j+i]
                    if section1 != section:
                        # No need to calculate other sections of this number of length i, can move on to next i.
                        could_be_valid = True
                    if j == length:
                        # Reached end of num with all sections of i length being equal - therefore invalid!
                        invalid = True
                    j += i
                
            i += 1
        if invalid:
            _sum += num

print("-"*10)
print(_sum)