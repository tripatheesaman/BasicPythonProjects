counts = dict()
fName = input('Enter the file name : ')
handle = open(fName)
for line in handle:
    word_list = line.split()
    for i in word_list:
        counts[i] = counts.get(i, 0) + 1
more_key = 0
more_value = 0
for key, value in counts.items():
    if more_value == 0 or value > more_value:
        more_key = key
        more_value = value
print(more_key, "has been repeated ", more_value, "times")
