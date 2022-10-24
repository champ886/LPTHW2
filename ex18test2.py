def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"argument 1: {arg1}, and argument2: {arg2}, and argument 3: {arg3}")

def print_two_again(arg1, arg2):
    print(f"""argument1: {arg1}
argument2: {arg2} """)

def print_one(arg1):
    print(f"{arg1} only")

def print_got_nothing():
    print("whatever you want")

print_two("Champion", "Nweke", "Julius")

print_two_again("Champion", "Nweke")

print_one("'Keiko'")

print_got_nothing()