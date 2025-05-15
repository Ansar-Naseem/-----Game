import random

points = 0
while(True):
    computer_move=random.randint(0,2)

    user_input=int(input("Enter snake(0),water(1) or gun(2) :"))
    lis = ["Snake","Water","Gun"]

    move_user = lis[user_input]
    move_computer = lis[computer_move]

    print("--------------------------------------------------------------------------------------------")
    print(f"Computer choose :{move_computer}\nUser choose :{move_user}")
    print("--------------------------------------------------------------------------------------------")

    #Logic :-
    # if(computer_move==user_input): --> for draw
    # elif(computer_move==0 and user_input==1 ):
    # elif(computer_move==0 and user_input==2 ): --> win --> -2
    # elif(computer_move==1 and user_input==0 ): --> win -->  1
    # elif(computer_move==1 and user_input==2 ):
    # elif(computer_move==2 and user_input==0 ): 
    # elif(computer_move==2 and user_input==1 ): --> win -->  1
    # we win when computer_move - user_input = -2 or 1 
        
    if(computer_move == user_input):
        print("Draw")

    else:
        if((computer_move - user_input) == 1 or (computer_move - user_input) == -2):
            print("Congrats You Win!!")
            points  += 1
        
        else:
            print("Sorry You Loss!!")
            break

print(f"Your Final score is {points}")