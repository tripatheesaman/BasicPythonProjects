choice = 'Y'
while choice == 'y' or choice == 'Y':
    c = 0
    symbol = input("What would you like to perform?")
    print('okay')
    a = float(input ('Enter the first number: '))
    b = float(input('Enter second number: '))
    if symbol == '+':
        c = a+b

    elif symbol == '-':
        c = a-b

    elif symbol == '/':
        c = a/b

    elif symbol == '*':
        c = a*b

    else:
        print('Invalid Symbol Pls try again.')

    if c != 0:
        print("The value you've been looking for is:", c)

    choice = input("Do you wanna do it again?(Y/N)")
