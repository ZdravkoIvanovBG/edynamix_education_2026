from datetime import datetime

date_str = input()

data = datetime.strptime(date_str, "%d.%m.%Y")

new_date = data.replace(year=data.year + 1)

print(f"New Date: {new_date.strftime('%d.%m.%Y')}")