from itertools import groupby
import copy

L = []
l = [None] * 2

for i in range(1, 7):
    l[0] = i
    for j in range(1, 7):
        l[1] = j
        L.append(copy.deepcopy(l))
print(L)
# things = [[1, 1], [1,1],[3, 1],[2,2] ,[2, 1],
#           [3, 1], [2,2],[1, 1]]
things = [("animal", "bear"),("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus"), ("animal", "duck")]

for key, group in groupby(things, key=lambda x: x[0]):
    print("key",key)
    print("group",list(group))
    # for g in group:
        # print("the sum is %s the num is %s" % (key, g))
