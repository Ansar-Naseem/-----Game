import random
points=0
while(True):

    computer_move=random.randint(0,2)
    # print(computer_move)

    user_input=int(input("Enter snake(0),water(1) or gun(2) :"))
    lis = ["Snake","Water","Gun"]

    move_user = lis[user_input]
    move_computer = lis[computer_move]

    print("--------------------------------------------------------------------------------------------")
    print(f"Computer choose :{move_computer}\nUser choose :{move_user}")
    print("--------------------------------------------------------------------------------------------")
    
    if(computer_move==user_input):
        print("Draw")
        
    elif(computer_move==0 and user_input==1 ):
        print("Sorry You Loss!!")
        break   
        
    elif(computer_move==0 and user_input==2 ):
        print("Congrats You Win!!")
        points  += 1
        
    elif(computer_move==1 and user_input==0 ):
        print("Congrats You Win!!")
        points += 1
        
    elif(computer_move==1 and user_input==2 ):
        print("Sorry You Loss!!")
        break
        
    elif(computer_move==2 and user_input==0 ):
        print("Sorry You Loss!!")
        break
        
    elif(computer_move==2 and user_input==1 ):
        print("Congrats You Win!!")
        points += 1

print(f"Your Final score is {points}")



