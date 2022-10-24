from sys import argv
pyhton_script, value1, value2, value3, value4, value5 = argv
print(">>> argv=", argv) 

print("This script is called ", pyhton_script)
print("The first variable ", value1)
print("The second variable is: ", value2)
print("The 3rd variable is: ", value3)
print("The fourth variable is: ", value4)
print(f"The fifth variable is  {value5}")

print(f"The folowing items {value1}, {value2} "
  f"{value3}, {value4}, {value5} were enterd by Champ")
