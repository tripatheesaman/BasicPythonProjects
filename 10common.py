di = dict()
lst = list()
fname = input('Enter name of the file: ')
handle = open(fname)
for line in handle:
    words = line.split()
    for i in words:
        di[i] = di.get(i, 0) + 1
for k, v in di.items():
    new_tup = (v, k)
    lst.append(new_tup)
sorted_ones = sorted(lst, reverse=True)
for k, v in sorted_ones[:10]:
    print(k, v)
