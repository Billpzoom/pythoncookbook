from collections import defaultdict

dl = defaultdict(list)

dl['a'].append(1)
dl['a'].append(2)
dl['b'].append(4)

ds = defaultdict(set)

ds['a'].add(1)
ds['a'].add(2)
ds['b'].add(4)

print(dl)
print(ds)