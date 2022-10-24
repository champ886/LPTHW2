from sys import argv

myscript, input_file = argv

current_file = open(input_file)
current_file_read = current_file.read()

readline_file = current_file.readline()
readline_file2 = current_file.readline()
readline_file3 = current_file.readline()


count_line = 1


print(count_line, readline_file)

count_line = count_line + 1

print(count_line)

print(count_line, readline_file2)

print(count_line)

print(count_line, readline_file3)