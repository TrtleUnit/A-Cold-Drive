def game():

    print ("You did a thing")
    print  ("Select A: I didn't do a thing")
    print  ("Select B: I did do a thing")
    Option = input  ("Select C: Did i do a thing?")

    if Option == ("A"):
        print ("You didn't do anything")
    elif Option == ("B"):
        print ("You did do something")
    elif Option == ("C"):
        print ("You are confused")
    else:
        print('error')
        game()
        
game()

