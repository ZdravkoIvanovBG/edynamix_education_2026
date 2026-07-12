def even_numbers(nums):
    return map(int, filter(lambda x: int(x) % 2 == 0, nums))

numbers = input().split(" ")

print(list(even_numbers(numbers)))