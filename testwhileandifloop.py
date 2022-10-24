i = 0

k = 7
check = False 

while True:

    

    answer = int(input("> "))
    #answerb = input("> ")
    #answer  = answer  + 4
    if answer  <= 2 and not check:
        print( "Really?")
        check = True
        print(check)
    elif answer == 7 and check:
        print ("Of course!")
           
        print(answer)
        print(check)
    elif answer  > 7 :
         print("answer >>", answer)
         print ("You changed it!")
         print(check)
    else:
        print("Start again!")
        exit(0)