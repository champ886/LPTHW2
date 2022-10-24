days = ['monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday','sunday']
names = ['keiko', 'champ', 'dave', 'brett', 'dan']

days_numbers = [1, 2, 3, 4, 5, 6, 7]


for day in days:
    print(f"Today is  {day}")

print("\n")

print("Thse are the names of my friends")
for name in names:
    print(f" Friend: {name}")

empty_list = []

for num in range(0, 11):
    print(f" my number is {num}")
    print(f"adding {num} to empty_list")
    empty_list.append(num)

print("\n")
print("num =", num)
for ele in empty_list:
    print(f"list item: {ele}")

