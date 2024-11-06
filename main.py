def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b > 0 else "divided by 0"

print('Sum:', sum(5, 5))
print('Subraction:', subtract(5, 5))
print('multiplication:', multiply(5, 5))
print('Dividing:', divide(5, 0))