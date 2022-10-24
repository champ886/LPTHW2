

my_five_things = "Boy champ me"

print("we need 5 things")

print("Convert to list")

things_five = my_five_things.split(" ")

print(things_five)

additional_things = ["six", "five", "four"]

while len(things_five) != 5:
    next_item = additional_things.pop(0)
    #print(additional_things.pop(0))
    things_five.append(next_item)
print(things_five)
print(len(things_five))

print(additional_things)


print(additional_things.pop(0))