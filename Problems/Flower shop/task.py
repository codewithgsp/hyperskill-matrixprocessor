import itertools

for i in range(1, 4):
    my_iter = itertools.combinations(flower_names, i)
    for j in my_iter:
        print(j)