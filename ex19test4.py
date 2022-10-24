def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly")
cheese_and_crackers(30, 40)

print("Or we can use variables from our script")
amount_of_cheese = 40
amount_cheese_boxes = 50

cheese_and_crackers(amount_of_cheese, amount_cheese_boxes)

print("We can also do some math")
cheese_and_crackers(20+30, 10+20)

print("And we can combine the two, variables and maths:")
cheese_and_crackers(amount_of_cheese + 40, amount_cheese_boxes + 10 + 20)

ten=10
twelve = 12

cheese_and_crackers(amount_of_cheese + ten, amount_cheese_boxes + ten + twelve)
cheese_and_crackers(ten, twelve)