import sys
lines = [l.strip() for l in sys.stdin.readlines()]

def flatten(l):
    return [i for sl in l for i in sl]

def is_separable(pairs):
    set1 = set()
    set2 = set()
    queue = set()
    # print(f"Unique items: {items}")
    set1.add(pairs[0][0])
    queue = set1.copy()
    while queue:
        item = queue.pop()
        subpairs = [p for p in pairs if item in p]
        while subpairs:
            pair = subpairs.pop()
            pairs.remove(pair)
            new_item = pair[1] if pair.index(item) == 0 else pair[0]
            queue.add(new_item)
            where_old = 1 if item in set1 else 2
            where_new = 1 if new_item in set1 else (2 if new_item in set2 else 0) 
            if where_old == where_new: 
                return False
            else:
                set1.add(new_item) if where_old == 2 else set2.add(new_item)
    return True    

t = 1
pairs = []
for i in range(len(lines)):
    if i == 0:
        continue
    if lines[i].isdigit():
        if not pairs:
            continue
        print(f"Case #{t}: {'Yes' if is_separable(pairs) else 'No'}")
        t += 1
        pairs = []
    else:
        pairs.append(lines[i].split())
print(f"Case #{t}: {'Yes' if is_separable(pairs) else 'No'}")
