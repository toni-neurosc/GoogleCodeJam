import sys
import utils

numbers = sys.stdin.readlines()[0].strip().split()

c = 0
np = numbers[0]
for i in range(1, len(numbers)):
    nc = numbers[i]
    print(f"np {np}, nc {nc}, c {c}")
    if nc < np:
        print('nc is smaller')
        c += 1
    np = nc if nc > np else np

print(f"Cost: {c}")