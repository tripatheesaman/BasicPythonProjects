string = input('Enter a string: ')
c = 0
for i in string:

    b = i
    if b == 'a':
        c = 1
        print('Letter found!')
        break
    print ('Still searching')
if c != 1:
    print('Not found sad ggs lol')
else:
    print('Nice one!')