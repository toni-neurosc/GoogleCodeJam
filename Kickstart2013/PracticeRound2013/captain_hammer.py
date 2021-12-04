import sys, math

lines = [l.strip() for l in sys.stdin.readlines()]

G = 9.8
for i in range(len(lines)):
    if i == 0:
        continue

    V, D = [int(n) for n in lines[i].split()]
    try:
        p = D*G/(V**2)
        p = 1 if p > 1 else p
        theta = math.degrees(math.asin(p)/2)
    except:
        print(V,D)

    print(f"Case #{i}: {theta}")
