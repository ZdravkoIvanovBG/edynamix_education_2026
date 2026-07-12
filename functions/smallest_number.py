#*numbers -> Packed into a tuple
def smallest_number(*numbers):
    return min(numbers)

a = int(input())
b = int(input())
c = int(input())

print(smallest_number(a, b, c))