days_of_week = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0
}

n = int(input())

for i in range(n):
    day = input()

    if day in days_of_week:
        days_of_week[day] += 1
    else:
        print("Invalid Day!")
        break

for day, count in days_of_week.items():
    if count > 0:
        print(f"{day} - {count}")