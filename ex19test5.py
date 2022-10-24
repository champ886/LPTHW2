def beans_and_rice(bags_of_beans, bags_of_rice):
    print(f"You have {bags_of_beans} bags of beans")
    print(f"You have {bags_of_rice} bags of rice")
    print("Jollof rice and beans!! Oiishi!!")
    print("if no be rice, na beans!.\n")

print("Just using numbers directly as arguments")
print("*" * 50)
beans_and_rice(49, 50)


print("Just using variables")
print("*" * 50)
amount_of_beans = 30
amount_of_rice = 50
beans_and_rice(amount_of_beans, amount_of_rice)

print("Use math:")
beans_and_rice(50+12, 400*9)

print("use variables and maths")
beans_and_rice(amount_of_beans + 60 * 30, amount_of_rice +60 * 50/2)

