a = int(input('enter the first number'))
b = int(input('Enter the second number'))


def add(x, y):
    return x + y


def odd(c):
    if (c % 2) == 1:
        print('New number is a odd number')
    else:
        print('New number is a even number')


odd(add(a, b))
