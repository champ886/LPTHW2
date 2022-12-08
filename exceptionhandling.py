x=1 #==> for incrementing

while True: # ==> condition
    # Action below==>
    try:
        filename = input("Which file would you like open?:")
        with open(filename, "r") as my_file:
            file_read = my_file.read()
    except FileNotFoundError:
        print(f"sorry, {filename} does not exist! Please try again!")

        # increment using x
        x = x + 1
        if x == 4:
            print ("Wrong filename 3 times.\nCheck name and Rerun")
            break
    else:
        print(file_read)
        break
   
