number = int(input())
country = input()

if country == "България":
    print(f"Крайна сума: {number * 1.02:.2f}")
elif country == "Европа":
    print(f"Крайна сума: {number * 1.05:.2f}")
else:
    print(f"Крайна сума: {number * 1.10:.2f}")