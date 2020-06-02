import random
computer_score=0
user_score=0

while True:
    option=['stone','paper','scissors']
    a=random.choice(option)
    user_input=input("Enter your choice 1.Stone 2.Paper 3.Scissors Press q to exit \n")
    
    if user_input.isdigit()==True:
        user_input=int(user_input)
        if option[user_input-1]==a:
            print("draw game")
            computer_score,user_score=computer_score,user_score
            print("Computer score:",computer_score,  " User score:", user_score )
        elif option[user_input-1]=='stone':
            if a=='paper':
                computer_score=computer_score+1
                print("Computer wins")
                print("Computer score:",computer_score,  " User score:", user_score )
                print("  ")
            elif a=='scissors':
                user_score=user_score+1
                print("User wins")
                print("Computer score:",computer_score,  " User score:", user_score )
                print("  ")
        elif option[user_input-1]=='paper':
            if a=='scissors':
                computer_score=computer_score+1
                print("Computer wins")
                print("Computer score:",computer_score,  " User score:", user_score )
                print("  ")
            elif a=='stone':
                user_score=user_score+1
                print("User wins")
                print("Computer score:",computer_score,  " User score:", user_score )
                print("  ")
        elif option[user_input-1]=='scissors':
                if a=='stone':
                    computer_score=computer_score+1
                    print("Computer wins")
                    print("Computer score:",computer_score,  " User score:", user_score )
                    print("  ")
                elif a=='paper':
                    user_score=user_score+1
                    print("User wins")
                    print("Computer score:",computer_score,  " User score:", user_score )
                    print("  ")     
    elif user_input.isdigit()==False:
                if str(user_input=='q'):
                    print("final score")
                    print("  ")
                    print("Computer score:",computer_score,  " User score:", user_score )
1                   quit()
    else:
            print("Invalid input sorry")
