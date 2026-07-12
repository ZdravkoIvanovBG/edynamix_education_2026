def sum_numbers(*numbers):
    return sum(numbers[:2]) #:2 is from 0 to 2 like a for cycle

def substract(*numbers):
    return sum_numbers(*numbers) - numbers[2]

def add_and_substract(*numbers):
    result = sum_numbers(*numbers)

    return substract(result, numbers[2])

a = int(input())
b = int(input())
c = int(input())

print(substract(a, b, c))