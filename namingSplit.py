items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)

print(a.start, a.stop, a.step)

print(items[2:4])
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)

s = 'Hello World!'
a = slice(5, 10, 2)
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])