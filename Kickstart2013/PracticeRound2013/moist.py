# Input
# The first line of the input gives the number of test cases, T. T test cases follow. 
# Each one starts with a line containing a single integer, N. 
# The next N lines each contain the name of a figure skater, in order from the top of the deck to the bottom.

# Output
# For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) 
# and y is the number of dollars it would cost Moist to use the robot to sort his deck of trading cards. 

import sys

def get_cost(l):
    
    c = 0
    vp = l[0]
    for i in range(1, len(l)):
        vc = l[i]
        if vc < vp:
            c += 1
        vp = vc if vc > vp else vp

    return c

lines = sys.stdin.readlines()
names = []
t = 1
for i in range(len(lines)):
    l = lines[i].strip()
    if i == 0:
        continue
    if l.isdigit():
        # print("check1")
        if names:
            # print("names true")
            print(f"Case #{t}: {(get_cost(names))}")
            N = l
            names = []
            t += 1
    else:
        # print("check2")
        names.append(l)

    # print(names)
print(f"Case #{t}: {(get_cost(names))}")

