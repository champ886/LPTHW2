#Formatter variable assigned for curly braces
formatter = "{} {} {} {}"

#Display formatted formatter using the .format function to display 1 2 3 4
# An error occurs if the intergers entered are not up to 4 spaces(index) as per "{} {} {} {}"
print(formatter.format(1, 2, 3,4))
#As above, but displaying strings ==> must be four spaces seperated by comma
print(formatter.format("one", "two", "three", "four"))
#As above, but displaying boolean ==> must be four spaces seperated by comma
print(formatter.format(True, False, False, True))
#As above, but this time only displaying the content of the formatter ==> must be four spaces seperated by comma
print(formatter.format(formatter, formatter, formatter, formatter))
#As above, but displaying string sentences in groups of four ==> must be four spaces, seperated by comma
print(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))