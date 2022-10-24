## Define Functions ==> Using Def

def test_asterisks(*tests):
    test1, test2 = tests
    print(f"show the values of test1 {test1} and test2", test2)

def test_2positions(test1, test2):
    print(f"test1 {test1} and test2 {test2}")

def test_1position(test1):
    print(f"{test1} is happy")

def test_none():
    print("I got nothing")


# Call functions using ==> 
# remove "def" from above
# pass an interger or a string to the postional parameters above
test_asterisks("Champ", "happy")
test_2positions("my", "man")
test_1position("champ")
test_none()