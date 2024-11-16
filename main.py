def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b > 0 else "divided by 0"

a = int(input('Enter a: '))
b = int(input('Enter b: '))

print('Sum:', sum(a, b))
print('Subraction:', subtract(a, b))
print('multiplication:', multiply(a, b))
print('Dividing:', divide(a, b))
