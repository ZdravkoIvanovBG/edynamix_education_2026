n = int(input())

numbers = []

for i in range(n):
    number = int(input())

    numbers.append(number)

print(f"Sum = {sum(numbers)}")