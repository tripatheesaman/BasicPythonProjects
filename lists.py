num_list = list()
while True:
    value = input('Enter the number')
    if value == 'done':
        break
    imp = float(value)
    num_list.append(imp)
length = len(num_list)
num_sum = sum(num_list)
average = num_sum/length
print("Average is :", average)


